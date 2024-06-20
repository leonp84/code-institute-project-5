from django.shortcuts import render


def home(request):
    template = 'main/index.html'
    context = {}
    return render(request, template, context)


def about(request):
    template = 'main/about.html'
    context = {}
    return render(request, template, context)
