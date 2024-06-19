from django.shortcuts import render


def all_products(request):
    context = {}
    return render(request, 'product/all_products.html', context)
