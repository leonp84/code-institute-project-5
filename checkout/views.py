from django.shortcuts import render
from django.http import JsonResponse
from product.models import Product
from .models import CheckoutSingleItem, Order
from my_account.forms import UserDetailsForm
from my_account.models import UserDetail
import json
import random
import datetime


def shopping_bag(request):
    request.session['watch_care_plan'] = False
    shopping_bag = request.session.get('shopping_bag', {})
    product_ids = [int(i) for i in shopping_bag.keys()]
    quantities = [int(i) for i in shopping_bag.values()]
    products_in_bag = Product.objects.filter(id__in=product_ids).order_by('id')

    context = {
      'products_in_bag': products_in_bag,
      'quantities': quantities
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


def checkout(request):
    shopping_bag = request.session.get('shopping_bag', {})
    product_ids = [int(i) for i in shopping_bag.keys()]
    quantities = [int(i) for i in shopping_bag.values()]

    # Generate an order number using today's date and a 6-digit random suffix
    order_number = ''
    order_number += str(datetime.date.today()).replace('-', '')[2:]
    order_number += '-'
    order_number += str(random.randrange(100000, 999999))

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

    single_items_queryset = CheckoutSingleItem.objects.filter(
      order_number=order_number)

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
        print('#######################')
        print(request.user)
        print(single_items_queryset)
        print(order_number)
        print(request.POST.get('user_first_name'))
        print(request.POST.get('user_last_name'))
        print(request.POST.get('user_phone_number'))
        print(request.POST.get('user_street_address1'))
        print(request.POST.get('user_street_address2'))
        print(request.POST.get('user_city'))
        print(request.POST.get('user_postcode'))
        print(request.POST.get('user_country'))
        print(request.POST.get('user_delivery_notes'))
        print(order_total)
        print(watch_care_plan_price)
        print(grand_total)
        print('** stripe_pid coming soon...')
        print('#######################')

        new_order = Order(
              user=(request.user if request.user.is_authenticated else None),
              order_number=order_number,
              first_name=request.POST.get('user_first_name'),
              last_name=request.POST.get('user_last_name'),
              phone_number=request.POST.get('user_phone_number'),
              street_address1=request.POST.get('user_street_address1'),
              street_address2=request.POST.get('user_street_address2'),
              city=request.POST.get('user_city'),
              postcode=request.POST.get('user_postcode'),
              country=request.POST.get('user_country'),
              delivery_notes=request.POST.get('user_delivery_notes'),
              order_total=order_total,
              watch_care_plan=(True if watch_care_plan_price > 0 else False),
              grand_total=grand_total,
              stripe_pid='** stripe_pid coming soon...',
        )
        new_order.save()
        print(new_order.items_ordered())
        return render(request, 'main/index.html')

    context = {
      'checkout_items': checkout_items,
      'order_total': order_total,
      'watch_care_plan_price': watch_care_plan_price,
      'grand_total': grand_total,
      'form': customer_details_form
    }
    template = 'checkout/checkout.html'
    return render(request, template, context)
