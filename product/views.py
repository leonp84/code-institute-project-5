from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
from my_account.models import UserDetail
from main.models import CustomerMessage
from django.contrib import messages
from .forms import ProductForm
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


def add_new_product(request):
    if request.method == 'POST':
        new_product = ProductForm(request.POST, request.FILES)
        if new_product.is_valid():
            new_product.save()
            messages.success(request,
                             'You have successfully added a new product',
                             extra_tags='STOREFRONT UPDATED')
        else:
            print(new_product.errors)
        return render(request, 'main/index.html')
      
    form = ProductForm()
    template = 'product/add_new_product.html'
    context = {'form': form}
    return render(request, template, context)


def delete_product(request, product_id):
    product = Product.objects.filter(id=product_id).first()

    if request.method == 'POST':
        product.delete()
        messages.info(request,
                      'This product has been removed from the store.',
                      extra_tags='PRODUCT DELETED')
        return render(request, 'main/index.html')

    context = {'product': product}
    return render(request, 'product/delete_product.html', context)


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
