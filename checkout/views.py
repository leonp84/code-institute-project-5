from django.shortcuts import render
from django.http import JsonResponse
from product.models import Product
from .models import CheckoutSingleItem
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
        new_item = CheckoutSingleItem(
          order_number=order_number,
          product=current_product,
          product_price=current_product.price,
          product_name_text=current_product.title,
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

    context = {
      'checkout_items': checkout_items,
      'order_total': order_total,
      'watch_care_plan_price': watch_care_plan_price,
      'grand_total': grand_total
    }
    template = 'checkout/checkout.html'
    return render(request, template, context)
