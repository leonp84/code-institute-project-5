from django.shortcuts import render, HttpResponse # noqa


def my_account(request):
    template = 'my_account/my_account.html'
    context = {}
    return render(request, template, context)
