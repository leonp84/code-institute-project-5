from django.http import JsonResponse
from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.dispatch import receiver
from django.contrib import messages
from allauth.account.signals import password_changed
from allauth.account.signals import user_logged_in, user_logged_out
import json
from checkout.models import Order
from product.models import Product
from main.models import DiscountCode
from .models import UserDetail
from .forms import UserDetailsForm


@login_required
def my_account(request):
    '''
    Renders Profile Page for logged in users
    **Context**
    ```wish_list```
    All entries in the many-to-many 'wish_list' field of
    :model:`my_account.UserDetail` for the current logged in user.
    ```past_orders```
    All instances of :model:`checkout.Order` filtered by the
    current logged in user.
    ```products```
    All instances of :model:`product.Product` to be used in the template
    if the current logged in user has superuser privileges (for product
    editing or deletion)
    **Template**
        :template:`my_account/my_account.html`
    '''
    current_user = UserDetail.objects.filter(user=request.user).first()
    products = Product.objects.all().order_by('watch_brand')
    wish_list = current_user.wish_list.all()
    past_orders = Order.objects.filter(email=request.user.email)

    template = 'my_account/my_account.html'
    context = {'wish_list': wish_list,
               'past_orders': past_orders,
               'products': products}
    return render(request, template, context)


@login_required
def update_profile(request):
    '''
    Allows logged users to update the instance of
    :model:`my_account.UserDetail` tied to their accounts.
    **Context**
    ```form```
    A single instance of :form:`my_account.UserDetailForm`. The (pre-populated)
    instance will be tied to the user account of the current logged in user.
    **Template**
        :template:`my_account/update_profile.html`
    '''
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
    '''
    This view is called by Javascript when a customer clicks
    the bookmark icon on any product_detail page. It then checks
    all entries in the many-to-many 'wish_list' field of
    :model:`my_account.UserDetail` for the current logged in user,
    and updates it accordingly. Details in /static/assets/js/product_detail.js
    If users are not logged in (and consequently no active wish_list is
    present) a JsonResponse message is returned and the customer informed
    via UI messaging.
    **Context**
        None - JsonResponse with status and message
    '''
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
    '''
    This view is called when a customer enters a discount
    code during the checkout process. It checks the received
    code against all instances of :model:`main.DiscountCode`.
    It then returns the appropriate JsonResponse allowing
    the UI to display messaging to the customer. Details in
    /static/assets/js/checkout.js
    **Context**
        None - JsonResponse with status and message
    '''
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
    '''
    Django allauth signal to display messaging upon password change
    '''
    messages.success(request,
                     'You have successfully changed your Password',
                     extra_tags='PASSWORD CHANGED')


@receiver(user_logged_in)
def logged_in_callbacl(sender, request, **kwargs):
    '''
    Django allauth signal to display messaging upon login
    '''
    messages.success(request,
                     'You have been successfully logged in',
                     extra_tags='LOGGED IN')


@receiver(user_logged_out)
def logged_out_callback(sender, request, **kwargs):
    '''
    Django allauth signal to display messaging upon logout
    '''
    messages.info(request,
                  'You have been successfully logged out',
                  extra_tags='LOGGED OUT')
