from django.shortcuts import render, reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib import messages
import json
import random
import datetime
import stripe
from my_account.forms import UserDetailsForm
from my_account.models import UserDetail
from product.models import Product
from checkout.models import Order
from .models import CheckoutSingleItem
from .forms import OrderForm


def shopping_bag(request):
    '''
    Displays the shopping bag for the current user.
    **Context**
    ```products_in_bag```
    A queryset of instances of :model:`product.Product` filtered
    by products currently in the user's shopping bag. To retrieve this,
    the session variable 'shopping_bag' is used throughout.
    ```quantities```
    The quantities (integers, in order) of each item in 'product_in_bag' used
    by the template for client side UI display.
    ```bag_empty```
    A boolean variable used by the template to display a specific
    message if the customers shopping bag is empty.
    **Template**
        :template:`checkout/shopping_bag.html`
    '''
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
    '''
    This view is called by Javascript when the customer clicks the
    'Buy this watch' button on any product_detail page. It receives
    the product_id of the product in question and updates the session
    variable 'shopping_bag' to add a new product, or update quantities.
    It also limits customers to max 3 of each product per Order.
    Details in /static/assets/js/product_detail.js
    **Context**
        None - JsonResponse with status and message
    '''
    if request.method == 'POST':
        data = json.load(request)
        product_to_add = str(data['product_id'])

        # Get and update shopping bag with django.sessions
        shopping_bag = request.session.get('shopping_bag', {})

        if product_to_add in shopping_bag.keys():
            # Check if 3 of product already in bag
            if shopping_bag[product_to_add] == 3:
                return JsonResponse({
                  'status': '403',
                  'message': 'Product Limit Reached'
                  })
            else:
                # Update quantity of items already in shopping bag
                shopping_bag[product_to_add] += 1
        else:
            # Create new item in shopping bag
            shopping_bag[product_to_add] = 1

        # Sort the shopping bag by product id before saving to session
        sorted_bag = dict(sorted(shopping_bag.items()))
        request.session['shopping_bag'] = sorted_bag

        return JsonResponse({
          'status': 'ok',
          'message': 'Item added to Shopping Bag'
          })


def update_shopping_bag(request):
    '''
    This view is called by Javascript whenever a customer removes
    an item from the shopping bag, or updates it quantities. It recreates
    the 'shopping_bag' session variable using product_id's and quantities sent
    by Javascript.
    Details in /static/assets/js/shopping_bag.js
    **Context**
        None - JsonResponse with message
    '''
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
    '''
    This view is called by Javascript whenever a customer clicks the
    'Watch Care Plan' checkbox in the checkout page. It updates the
    'watch_care_plan' session variable accordingly, to later be used in the
    checkout view below.
    Details in /static/assets/js/shopping_bag.js
    **Context**
        None - JsonResponse with message
    '''
    if request.method == 'POST':
        data = json.load(request)
        updated_plan = data['watch_care_plan']
        request.session['watch_care_plan'] = updated_plan
        return JsonResponse({'message': 'Watch Care Plan Updated'})


def checkout(request):
    '''
    Displays the checkout page for the current user. During the POST request
    method this view caches the order details by creation a session variable
    'cached_order' which is then later retrieved by the order_confirmation view
    after successful payment of the order.
    **Context**
    ```checkout_items```
    Queryset of :model:`checkout.SingleCheckoutItem` filtered by
    the current order number. Both the items in the queryset, and
    the order number are generated/saved during the GET request of
    this view.
    ```order_total```
    An integer representing the current order (sub)total based
    on the current items in the shopping bag, and the quantities of
    each item. The latter two variables are retrieved from the session
    variable 'shopping_bag'.
    ```watch_care_plan_price```
    An integer representing 2.5% of 'order_total', but only if
    the 'watch_care_plan' session variable is set to True.
    ```grand_total```
    An integer representing the total of order_total and watch_care_plan_price
    ```form```
    A single instance of :form:`my_account.UserDetailsForm` pre-populated if
    the user is logged in and have provided the relevant information after
    account creation.
    **Template**
        :template:`checkout/checkout.html`
    '''
    shopping_bag = request.session.get('shopping_bag', {})
    product_ids = [int(i) for i in shopping_bag.keys()]
    quantities = [int(i) for i in shopping_bag.values()]

    # Generate an order number using today's date and a 6-digit random suffix
    order_number = ''
    order_number += str(datetime.date.today()).replace('-', '')[2:]
    order_number += '-'
    order_number += str(random.randrange(100000, 999999))
    # Store Order Number in session to update model after payment
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
        # Update the order total after each new CheckoutSingleItem is created
        order_total += new_item.subtotal()

    watch_care_plan_price = 0
    # Update watch_care_plan_price (2.5% of total) if the user chose the plan
    if request.session.get('watch_care_plan'):
        watch_care_plan_price = int(order_total / 100 * 2.5)

    grand_total = order_total + watch_care_plan_price

    # checkout_items is used by the template to display product information.
    checkout_items = CheckoutSingleItem.objects.filter(
      order_number=order_number)

    # Select pre-populated form if the customer is logged in.
    if request.user.is_authenticated:
        current_user = UserDetail.objects.filter(user=request.user).first()
        customer_details_form = UserDetailsForm(instance=current_user)
    else:
        customer_details_form = UserDetailsForm()

    if request.method == 'POST':

        new_order_info = {
            'user': None,
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
            'grand_total': request.POST.get('grand_total').replace(',', ''),
            'stripe_pid': '',
        }

        # Cache order information in session variable
        request.session['cached_order'] = new_order_info

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


def order_payment(request):
    '''
    Displays a payment screen allowing users to enter credit card details.
    More details in /static/assets/js/checkout_stripe.js
    **Context**
    ```grand_total```
    An integer of the final amount to be paid by the customer.
    Used by stripe to create a new payment instance.
    **Template**
        :template:`checkout/order_payment.html`
    '''
    cached_order = request.session.get('cached_order')
    grand_total = int(cached_order['grand_total'])
    context = {'grand_total': grand_total}
    template = 'checkout/order_payment.html'
    return render(request, template, context)


def checkout_data(request):
    '''
    This view is called from checkout_stripe.js when the stripe JS script
    creates a new payment instance. The view retrieves the grand total amount
    from the order_payment.html page and sends it back to stripe as part of a
    'clientSecret' variable (via JsonResponse) that Stripe needs to create
    the payment instance.
    **Context**
        None - JsonResponse with message
    '''
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
    '''
    Creates a new instance of :model:`checkout.Order` and displays the
    order confirmation page for customers who have successfully
    made payment. The redirect to this view is done by Stripe.
    This view also handles sending order confirmation emails.
    See /static/assets/js/checkout_stripe.js for more details.
    **Context**
    ```paid_order```
    The newly created instance of :model:`checkout.Order` with all
    details of the order displayed then used by the template.
    **Template**
        :template:`checkout/shopping_bag.html`
    '''
    payment_intent = request.GET['payment_intent']
    request.session['cached_order']['stripe_pid'] = payment_intent
    cached_order = request.session.get('cached_order')
    paid_order_form = OrderForm(data=cached_order)
    if paid_order_form.is_valid():
        paid_order_form.save()
    else:
        print(paid_order_form.errors)

    paid_order = Order.objects.filter(stripe_pid=payment_intent).first()

    # Assign order to user, including newly created user if applicable
    if User.objects.filter(email=paid_order.email).exists():
        paid_order.user = User.objects.filter(email=paid_order.email).first()

    paid_order.save()

    # Send Order Confirmation Email
    subject = 'Order Confirmed | Heritage Company'
    message = render_to_string(
        'checkout/email_confirmation/email_confirmation.html',
        {'paid_order': paid_order,
         'our_email': settings.DEFAULT_FROM_EMAIL})

    send_mail(
        subject=subject,
        html_message=message,
        message='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[paid_order.email],
        )

    context = {'paid_order': paid_order}
    template = 'checkout/order_confirmation.html'
    return render(request, template, context)


def generate_password():
    '''
    This function is used by the checkout view to generate a unique,
    strong, temporary password for customers who wish to create an
    account upon order completion. It returns the newly generated
    password as a string.
    '''
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
