from .forms import UserDetailsForm
from .models import UserDetail

from django.shortcuts import render, HttpResponse # noqa
from allauth.account.signals import password_changed
from allauth.account.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.contrib import messages


def my_account(request):
    template = 'my_account/my_account.html'
    context = {}
    return render(request, template, context)


def update_profile(request):
    current_user = UserDetail.objects.filter(user=request.user).first()

    if request.method == 'POST':
        update_user = UserDetailsForm(data=request.POST, instance=current_user)
        if update_user.is_valid():
            update_user.save()
            messages.success(request,
                             'Your Profile and Delivery Adress\
                              have been successfully updated',
                             extra_tags='PROFILE UPDATED')
        else:
            print(update_user.errors)
            messages.warning(request,
                             'Your profile could not be updated, please\
                              check your information and try again.\
                              If the problem persists, please contact us.',
                             extra_tags='ERROR')

    form = UserDetailsForm(instance=current_user)
    template = 'my_account/update_profile.html'
    context = {'form': form}
    return render(request, template, context)


@receiver(password_changed)
def password_change_callback(sender, request, **kwargs):
    messages.success(request,
                     'You have Successfully changed your Password',
                     extra_tags='PASSWORD CHANGED')


@receiver(user_logged_in)
def logged_in_callbacl(sender, request, **kwargs):
    messages.success(request,
                     'You have been Successfully logged in',
                     extra_tags='LOGGED IN')


@receiver(user_logged_out)
def logged_out_callback(sender, request, **kwargs):
    messages.info(request,
                  'You have been Successfully logged out',
                  extra_tags='LOGGED OUT')
