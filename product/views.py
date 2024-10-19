from django.shortcuts import render, reverse, HttpResponseRedirect
# Import below used to check for superuser status
from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
import json
from my_account.models import UserDetail
from main.models import CustomerMessage
from .models import Product
from .forms import ProductForm


def all_products(request, sort_by='title'):
    '''
    Displays all instances of :model:`product.Product`
   **Context**
    ```products```
        A queryset of all instances of :model:`product.Product`
        sorted by the `sort_by` variable (default = 'title')
    **Template**
        :template:`product/all_products.html`
    '''
    products = Product.objects.all().order_by(sort_by)
    context = {'products': products}
    return render(request, 'product/all_products.html', context)


def breitling(request, sort_by='title'):
    '''
    Displays all instances of :model:`product.Product` with a filter
    applied to retrieve products of brand 'BR' (Breitling)
    **Context**
    ```products```
        A queryset of all filtered instances of :model:`product.Product`
        sorted by the `sort_by` variable (default = 'title')
    **Template**
        :template:`product/breitling.html`
    '''
    products = Product.objects.filter(watch_brand='BR').order_by(sort_by)
    context = {'products': products}
    return render(request, 'product/breitling.html', context)


def tag_heuer(request, sort_by='title'):
    '''
    Displays all instances of :model:`product.Product` with a filter
    applied to retrieve products of brand 'TA' (Tag Heuer)
    **Context**
    ```products```
        A queryset of all filtered instances of :model:`product.Product`
        sorted by the `sort_by` variable (default = 'title')
    **Template**
        :template:`product/tag_heuer.html`
    '''
    products = Product.objects.filter(watch_brand='TA').order_by(sort_by)
    context = {'products': products}
    return render(request, 'product/tag_heuer.html', context)


def omega(request, sort_by='title'):
    '''
    Displays all instances of :model:`product.Product` with a filter
    applied to retrieve products of brand 'OM' (Omega)
    **Context**
    ```products```
        A queryset of all filtered instances of :model:`product.Product`
        sorted by the `sort_by` variable (default = 'title')
    **Template**
        :template:`product/omega.html`
    '''
    products = Product.objects.filter(watch_brand='OM').order_by(sort_by)
    context = {'products': products}
    return render(request, 'product/omega.html', context)


def tissot(request, sort_by='title'):
    '''
    Displays all instances of :model:`product.Product` with a filter
    applied to retrieve products of brand 'TI' (Tissot)
    **Context**
    ```products```
        A queryset of all filtered instances of :model:`product.Product`
        sorted by the `sort_by` variable (default = 'title')
    **Template**
        :template:`product/tissot.html`
    '''
    products = Product.objects.filter(watch_brand='TI').order_by(sort_by)
    context = {'products': products}
    return render(request, 'product/tissot.html', context)


def sale(request, sort_by='title'):
    '''
    Displays all instances of :model:`product.Product` with a filter
    applied to retrieve discounted products (`discount_percentage__gt=0`)
    **Context**
    ```products```
        A queryset of all filtered instances of :model:`product.Product`
        sorted by the `sort_by` variable (default = 'title')
    **Template**
        :template:`product/sale.html`
    '''
    products = Product.objects.filter(
      discount_percentage__gt=0).order_by(sort_by)
    context = {'products': products}
    return render(request, 'product/sale.html', context)


def product_detail(request, product_id):
    '''
    Displays one instances of :model:`product.Product` filtered
    using the parameter `product_id`
    **Context**
    ```product```
        A single instance of :model:`product.Product`
    ```bookmarked```
        A boolean variable used in the template to display
        elements based on wether the user has bookmarked this
        specific instance of :model:`product.Product`
    **Template**
        :template:`product/product_detail.html`
    '''
    if Product.objects.filter(pk=product_id).exists():

        bookmarked = False
        if request.user.is_authenticated:
            current_user = UserDetail.objects.filter(user=request.user).first()
            if current_user.wish_list.filter(id=product_id).exists():
                bookmarked = True
        product = Product.objects.filter(pk=product_id).first()
        context = {'product': product,
                   'bookmarked': bookmarked}

        return render(request, 'product/product_detail.html', context)
    else:
        return render(request, '404.html')


@user_passes_test(lambda u: u.is_superuser)
def add_new_product(request):
    '''
    Allows creation of one new instance of :model:`product.Product`
    This view is restricted to superusers.
    **Context**
    ```form```
        A single instance of :form:`product.ProductForm`
    **Template**
        :template:`product/add_new_product.html`
    '''
    if request.method == 'POST':
        new_product = ProductForm(request.POST, request.FILES)
        if new_product.is_valid():
            product = new_product.save()
            messages.success(request,
                             'You have successfully added a new product',
                             extra_tags='STOREFRONT UPDATED')
        else:
            print(new_product.errors)
        return HttpResponseRedirect(reverse(
          'product_detail', args=[product.id]))

    form = ProductForm()
    template = 'product/add_new_product.html'
    context = {'form': form}
    return render(request, template, context)


@user_passes_test(lambda u: u.is_superuser)
def edit_product(request, product_id):
    '''
    Allows editing of one existing instance of :model:`product.Product`
    This view is restricted to superusers.
    **Context**
    ```form```
        A single instance of :form:`product.ProductForm` retrieved
        by using the variable `product_id` as filter
    **Template**
        :template:`product/edit_product.html`
    '''
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


@user_passes_test(lambda u: u.is_superuser)
def delete_product(request, product_id):
    '''
    Allows deletion of one existing instance of :model:`product.Product`
    This view is restricted to superusers and only called after user
    has passed - in line with defensive programming - an extra confirmation
    **Context**
    ```product```
        A single instance of :model:`product.Product` retrieved by using
        the variable 'product_id' as filter
    **Template**
        :template:`product/delete_product.html`
    '''
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
    '''
    Allows creation of one new instance of :model:`main.CustomerMessage`
    Details in /static/assets/js/product_detail.js
    **Context**
    JsonResponse with success message
    **Template**
        None - Jsonresponse
    '''
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

    return JsonResponse({'message': 'Customer Message Received'})


def search(request):
    '''
    Allows users to search through all instances of :model:`product.Product`
    **Context**
    ```search_results```
        A queryset of filtered instances of :model:`product.Product` using
        the POST variable 'search-input' as keyword filter.
    ```count```
        An integer of the total number of found items - the length of
        'search_results'
    ```user_query```
        A string of the original search term entered by the user
    **Template**
        :template:`product/search_results.html`
    '''
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
    '''
    Allows users to do filtered search through all instances of
    model:`product.Product`
    **Context**
    ```search_results```
        A queryset of filtered instances of :model:`product.Product` using
        six POST variables retrieved upon form submission by the user
    ```count```
        An integer of the total number of found items - the length of
        'search_results'
    ```user_query```
        A string of the original search term entered by the user
        (edited, if left empty, for UI clarity)
    **Template**
        :template:`product/search_results.html`
    '''
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        brand = request.POST.get('brand').split(',')
        gender = request.POST.get('gender').split(',')
        dial_color = request.POST.get('dial_color').split(',')
        min_price = request.POST.get('min-price')
        max_price = request.POST.get('max-price')
        queryset = Product.objects.filter(
            (Q(title__icontains=keyword) | Q(desc__icontains=keyword)),
            watch_brand__in=brand,
            watch_gender__in=gender,
            watch_dial_colour__in=dial_color,
            price__gte=min_price,
            price__lte=max_price,
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
