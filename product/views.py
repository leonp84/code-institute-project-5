from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
from my_account.models import UserDetail
from main.models import CustomerMessage
import json


def all_products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product/all_products.html', context)


def product_detail(request, product_id):
    bookmarked = False
    if request.user.is_authenticated:
        current_user = UserDetail.objects.filter(user=request.user).first()
        if current_user.wish_list.filter(id=product_id).exists():
            bookmarked = True
    product = Product.objects.filter(pk=product_id).first()
    context = {'product': product,
               'bookmarked': bookmarked}

    return render(request, 'product/product_detail.html', context)


def sale(request):
    products = Product.objects.filter(discount_percentage__gt=0)
    context = {'products': products}
    return render(request, 'product/sale.html', context)


def customer_product_message(request):
    if request.method == 'POST':
        data = json.load(request)
        customer_name = data['customer_name']
        customer_email = data['customer_email']
        product_name = data['product_name']
        product_ref = data['product_ref']
        customer_message = data['customer_message']

    new_customer_message = CustomerMessage(
        customer_name=customer_name,
        customer_email=customer_email,
        product_name=product_name,
        product_ref=product_ref,
        customer_message=customer_message,
    )
    new_customer_message.save()

    return JsonResponse({'message': 'Model Updated'})
