from django.shortcuts import render, HttpResponse # noqa
from allauth.account.signals import password_changed
from django.dispatch import receiver
from django.contrib import messages


def my_account(request):
    template = 'my_account/my_account.html'
    context = {}
    return render(request, template, context)


@receiver(password_changed)
def password_change_callback(sender, request, **kwargs):
    print('Your password has been changed!')
    messages.success(request, 'You have Successfully changed your Password!')
