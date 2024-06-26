from .forms import UserDetailsForm
from .models import UserDetail
from django.http import JsonResponse
from django.shortcuts import render, reverse, HttpResponseRedirect
from allauth.account.signals import password_changed
from allauth.account.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.contrib import messages
from product.models import Product
from main.models import DiscountCode
import json


def my_account(request):

    current_user = UserDetail.objects.filter(user=request.user).first()
    products = Product.objects.all()
    wish_list = current_user.wish_list.all()
    template = 'my_account/my_account.html'
    context = {'wish_list': wish_list,
               'products': products}
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

        return HttpResponseRedirect(reverse('my_account', args=[]))

    form = UserDetailsForm(instance=current_user)
    template = 'my_account/update_profile.html'
    context = {'form': form}
    return render(request, template, context)


def add_bookmarked_item(request):
    if request.method == 'POST':
        data = json.load(request)
        product_id = data['product_id']

        if request.user.is_authenticated:
            current_user = UserDetail.objects.filter(user=request.user).first()
            new_product = Product.objects.filter(id=product_id).first()

            if current_user.wish_list.filter(id=product_id).exists():
                current_user.wish_list.remove(new_product)
                return_message = 'Item REMOVED from your wish list'
            else:
                current_user.wish_list.add(new_product)
                return_message = 'Item ADDED to your wish list'

            return JsonResponse({
              'status': 'ok',
              'message': return_message
              })
        else:
            return JsonResponse({
              'status': '406',
              'message': 'User needs to log in'
              })


def check_discount_code(request):
    if request.method == 'POST':
        data = json.load(request)
        code = data['code']

        if DiscountCode.objects.filter(discount_code=code).exists():
            found_code = DiscountCode.objects.filter(
              discount_code=code).first()
            found_code.delete()
            return JsonResponse({
              'status': 'ok',
              'message': 'Code Accepted'
              })
        else:
            return JsonResponse({
              'status': '406',
              'message': 'Code Invalid'
              })


@receiver(password_changed)
def password_change_callback(sender, request, **kwargs):
    messages.success(request,
                     'You have successfully changed your Password',
                     extra_tags='PASSWORD CHANGED')


@receiver(user_logged_in)
def logged_in_callbacl(sender, request, **kwargs):
    messages.success(request,
                     'You have been successfully logged in',
                     extra_tags='LOGGED IN')


@receiver(user_logged_out)
def logged_out_callback(sender, request, **kwargs):
    messages.info(request,
                  'You have been successfully logged out',
                  extra_tags='LOGGED OUT')
