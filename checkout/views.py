from django.shortcuts import render
from django.http import JsonResponse
from product.models import Product
import json


def checkout(request):
    shopping_bag = request.session.get('shopping_bag', {})
    product_ids = [int(i) for i in shopping_bag.keys()]
    quantities = [int(i) for i in shopping_bag.values()]
    products_in_bag = Product.objects.filter(id__in=product_ids).order_by('id')

    context = {
      'products_in_bag': products_in_bag,
      'quantities': quantities
    }
    template = 'checkout/checkout.html'
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
