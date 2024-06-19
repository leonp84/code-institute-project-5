from django.shortcuts import render
from .models import Product


def all_products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product/all_products.html', context)


def product_detail(request, product_id):
    product = Product.objects.filter(pk=product_id).first()
    context = {'product': product}
    return render(request, 'product/product_detail.html', context)
