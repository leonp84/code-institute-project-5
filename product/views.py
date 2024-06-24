from django.shortcuts import render, reverse, HttpResponseRedirect
from django.http import JsonResponse
from .models import Product
from my_account.models import UserDetail
from main.models import CustomerMessage
from django.contrib import messages
from django.db.models import Q
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


def edit_product(request, product_id):
    product = Product.objects.filter(id=product_id).first()
    if request.method == 'POST':
        updated_product = ProductForm(
          request.POST, request.FILES, instance=product)
        if updated_product.is_valid():
            updated_product.save()
            messages.success(request,
                             'You have successfully updated this product',
                             extra_tags='STOREFRONT UPDATED')
        else:
            print(updated_product.errors)

        return HttpResponseRedirect(reverse(
          'product_detail', args=[product_id]))

    form = ProductForm(instance=product)
    template = 'product/edit_product.html'
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


def search(request):
    if request.method == 'POST':
        user_search = request.POST.get('search-input')
        search_results = Product.objects.filter(
            title__icontains=user_search) | Product.objects.filter(
            desc__icontains=user_search)

        count = len(search_results)

        return render(
            request,
            'product/search_results.html',
            {'search_results': search_results,
             'count': count,
             'user_query': user_search}
             )


def advanced_search(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        gender = request.POST.get('gender')
        brand = request.POST.get('brand')
        dial_color = request.POST.get('dial_color')
        min_price = request.POST.get('min-price')
        max_price = request.POST.get('max-price')

        queryset = Product.objects.filter(
          (Q(title__icontains=keyword) | Q(desc__icontains=keyword)) &
          Q(watch_brand=brand) &
          Q(watch_gender__icontains=gender) &
          Q(watch_dial_colour__icontains=dial_color) &
          Q(price__gte=min_price) &
          Q(price__lte=max_price)
        )
        count = len(queryset)
        messages.info(request,
                      'Your search filters have been applied to this result.',
                      extra_tags='ADVANCED SEARCH')

        if keyword == '':
            keyword = '(No Keyword Given)'

        return render(
            request,
            'product/search_results.html',
            {'search_results': queryset,
             'count': count,
             'user_query': keyword}
             )

    return render(request, 'product/advanced_search.html')
