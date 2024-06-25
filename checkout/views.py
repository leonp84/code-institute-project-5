from django.shortcuts import render
from django.http import JsonResponse
import json


def checkout(request):
    del request.session['shopping_bag']
    context = {}
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
            print('already in the bag')
        else:
            # Create new item in shopping bag
            shopping_bag[product_to_add] = 1
            print('new product')

        request.session['shopping_bag'] = shopping_bag

        check_again = request.session.get('shopping_bag', {})
        print('##########')
        print(check_again)
        print('##########')
        return JsonResponse({'message': 'Item added to Shopping Bag'})
