from django.shortcuts import render


def home(request):
    template = 'main/index.html'
    context = {}
    return render(request, template, context)


def about(request):
    template = 'main/about.html'
    context = {}
    return render(request, template, context)


def privacy_policy(request):
    template = 'main/privacy_policy.html'
    context = {}
    return render(request, template, context)


def terms_and_conditions(request):
    template = 'main/terms_and_conditions.html'
    context = {}
    return render(request, template, context)
