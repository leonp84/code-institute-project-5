from django.shortcuts import render, reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseRedirect
from product.models import Product
from .models import CheckoutSingleItem, Order
from .forms import OrderForm
from django.conf import settings
from my_account.forms import UserDetailsForm
from my_account.models import UserDetail
from django.contrib import messages
import json
import random
import datetime
import stripe


def shopping_bag(request):
    request.session['watch_care_plan'] = False
    shopping_bag = request.session.get('shopping_bag', {})
    product_ids = [int(i) for i in shopping_bag.keys()]
    quantities = [int(i) for i in shopping_bag.values()]
    products_in_bag = Product.objects.filter(id__in=product_ids).order_by('id')

    bag_empty = True
    if len(products_in_bag) > 0:
        bag_empty = False
    else:
        bag_empty = True
    context = {
      'products_in_bag': products_in_bag,
      'quantities': quantities,
      'bag_empty': bag_empty
    }
    template = 'checkout/shopping_bag.html'
    return render(request, template, context)


def add_item_to_bag(request):
    if request.method == 'POST':
        data = json.load(request)
        product_to_add = str(data['product_id'])

        # Get and update shopping bag with django.sessions
        shopping_bag = request.session.get('shopping_bag', {})

        print(shopping_bag.keys())

        if product_to_add in shopping_bag.keys():
            # Update quantity of items already in shopping bag
            shopping_bag[product_to_add] += 1
        else:
            # Create new item in shopping bag
            shopping_bag[product_to_add] = 1

        # Sort the shopping bag by product id before saving to session
        sorted_bag = dict(sorted(shopping_bag.items()))
        request.session['shopping_bag'] = sorted_bag

        return JsonResponse({'message': 'Item added to Shopping Bag'})


def update_shopping_bag(request):
    if request.method == 'POST':
        data = json.load(request)
        updated_products = data['updated_products']
        updated_quantities = data['updated_quantities']
        new_bag = {}
        for i in range(len(updated_products)):
            new_bag[updated_products[i]] = int(updated_quantities[i])

        request.session['shopping_bag'] = new_bag

        return JsonResponse({'message': 'Shopping Bag Updated'})


def update_watch_care_plan(request):
    if request.method == 'POST':
        data = json.load(request)
        updated_plan = data['watch_care_plan']
        request.session['watch_care_plan'] = updated_plan
        return JsonResponse({'message': 'Watch Care Plan Updated'})


def checkout_data(request):
    data = json.loads(request.body)
    amount = data['amount']
    stripe.api_key = settings.STRIPE_SECRET_KEY
    intent = stripe.PaymentIntent.create(
        amount=amount,
        currency='usd',
    )

    return JsonResponse({
        'clientSecret': intent['client_secret'],
        'status_code': 200
    })


def order_confirmation(request, params):
    order_number = request.session.get('order_number')
    paid_order = Order.objects.filter(order_number=order_number).first()
    print(paid_order.stripe_pid)
    paid_order.stripe_pid = "Payment is done, whohoo!"
    print(paid_order.stripe_pid)
    paid_order.save()

    # Send Order Confirmation Email
    # subject = 'Order Confirmed | Heritage Company'
    # message = render_to_string(
    #     'checkout/email_confirmation/email_confirmation.html',
    #     {'new_order': new_order,
    #       'our_email': settings.DEFAULT_FROM_EMAIL})

    # send_mail(
    #     subject=subject,
    #     html_message=message,
    #     message='',
    #     from_email=settings.DEFAULT_FROM_EMAIL,
    #     recipient_list=[new_order.email],
    #     )
    context = {'new_order': paid_order}
    template = 'checkout/order_confirmation.html'
    return render(request, template, context)


def order_payment(request):
    order_number = request.session.get('order_number')
    unpaid_order = Order.objects.filter(order_number=order_number).first()
    context = {'new_order': unpaid_order}
    template = 'checkout/order_payment.html'
    return render(request, template, context)


def checkout(request):
    shopping_bag = request.session.get('shopping_bag', {})
    product_ids = [int(i) for i in shopping_bag.keys()]
    quantities = [int(i) for i in shopping_bag.values()]

    # Generate an order number using today's date and a 6-digit random suffix
    order_number = ''
    order_number += str(datetime.date.today()).replace('-', '')[2:]
    order_number += '-'
    order_number += str(random.randrange(100000, 999999))
    # Store Order Number in session to update model in after payment
    request.session['order_number'] = order_number

    order_total = 0

    for i in range(len(product_ids)):
        current_product = Product.objects.filter(id=product_ids[i]).first()
        name_text = (f"{current_product.get_watch_brand_display().upper()} "
                     f"{current_product.title}")
        new_item = CheckoutSingleItem(
          order_number=order_number,
          product=current_product,
          product_price=current_product.price,
          product_name_text=name_text,
          product_ref_text=current_product.ref,
          quantity=quantities[i]
        )
        new_item.save()
        order_total += new_item.subtotal()

    watch_care_plan_price = 0
    if request.session.get('watch_care_plan'):
        watch_care_plan_price = int(order_total / 100 * 2.5)

    grand_total = order_total + watch_care_plan_price

    checkout_items = CheckoutSingleItem.objects.filter(
      order_number=order_number)

    if request.user.is_authenticated:
        current_user = UserDetail.objects.filter(user=request.user).first()
        customer_details_form = UserDetailsForm(instance=current_user)
    else:
        customer_details_form = UserDetailsForm()

    if request.method == 'POST':

        new_order = OrderForm({
            'user': request.user if request.user.is_authenticated else None,
            'order_number': order_number,
            'first_name': request.POST.get('user_first_name'),
            'last_name': request.POST.get('user_last_name'),
            'email': request.POST.get('user_email'),
            'phone_number': request.POST.get('user_phone_number'),
            'street_address1': request.POST.get('user_street_address1'),
            'street_address2': request.POST.get('user_street_address2'),
            'city': request.POST.get('user_city'),
            'postcode': request.POST.get('user_postcode'),
            'country': request.POST.get('user_country'),
            'delivery_notes': request.POST.get('user_delivery_notes'),
            'order_total': order_total,
            'watch_care_plan': (True if watch_care_plan_price > 0 else False),
            'grand_total': grand_total,
            'stripe_pid': '** stripe_pid coming soon...',
        })

        if request.POST.get('create_new_account') == 'True':
            # Create New User Account (with temporary password)
            temp_passw = generate_password()

            # Check if new account email already exists, and return error if so
            new_email = request.POST.get('user_email')
            if User.objects.filter(email=new_email).exists():
                messages.error(request, 'That account already exists! Please'
                                        ' sign in and try again.',
                                        extra_tags='ERROR')
                return render(request, 'main/index.html')

            new_user = User.objects.create_user(
                        username=request.POST.get('user_email'),
                        email=request.POST.get('user_email'),
                        password=temp_passw)
            new_user.save()

            # Complete New User Account Details using Order Details
            new_user_info = UserDetail.objects.filter(user=new_user).first()
            new_user_info.user_first_name = request.POST.get('user_first_name')
            new_user_info.user_last_name = request.POST.get('user_last_name')
            new_user_info.user_phone_number = request.POST.get(
              'user_phone_number')
            new_user_info.user_street_address1 = request.POST.get(
              'user_street_address1')
            new_user_info.user_street_address2 = request.POST.get(
              'user_street_address2')
            new_user_info.user_city = request.POST.get('user_city')
            new_user_info.user_postcode = request.POST.get('user_postcode')
            new_user_info.user_country = request.POST.get('user_country')
            new_user_info.save()

            # Assign new Order to newly registered User
            new_order.user = new_user

            # Send New Account Creation Confirmation Email
            subject = 'Account Created | Heritage Company'
            message = render_to_string(
                'checkout/email_confirmation/email_account.html',
                {'user_name': new_user.username,
                 'temp_passw': temp_passw})

            # Users are instructed to change/personalize their password ASAP.
            send_mail(
                subject=subject,
                html_message=message,
                message='',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[new_user.email],
                )
        if new_order.is_valid():
            new_order.save()
        else:
            print(new_order.errors)

        return HttpResponseRedirect(reverse('order_payment', args=[]))

    context = {
      'checkout_items': checkout_items,
      'order_total': order_total,
      'watch_care_plan_price': watch_care_plan_price,
      'grand_total': grand_total,
      'form': customer_details_form
    }
    template = 'checkout/checkout.html'
    return render(request, template, context)


def generate_password():
    p1 = [i for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    p2 = [i for i in 'abcdefghijklmnopqrstuvwxyz']
    p3 = [i for i in '0123456789']
    p4 = [i for i in '!@#$%^&*()-_=[]|;:,.<>?/~`"']
    p5 = [p1, p2, p3, p4]

    new_password = ''
    for i in range(10):
        item = random.choice(p5)
        new_password += random.choice(item)

    return new_password
