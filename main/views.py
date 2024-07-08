from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
import random
import json
from product.models import Product
from .forms import NewsLetterSignupsForm, CustomerMessageForm
from .models import NewsLetterSignup, DiscountCode


def about(request):
    '''
    Renders About Us Page
    **Template**
        :template:`main/about.html`
    '''
    template = 'main/about.html'
    context = {}
    return render(request, template, context)


def contact_us(request):
    '''
    Renders Contact Us Page
    **Context**
    ```form```
    One instance of :form:`forms.CustomerMessageForm`
    **Template**
        :template:`main/contact_us.html`
    '''
    if request.method == 'POST':
        new_message = CustomerMessageForm(data=request.POST)
        if new_message.is_valid:
            new_message.save()
            messages.success(request, 'Thank you for contacting us.\
                                       We will reply within 48 hours.',
                                      extra_tags='MESSAGE SENT')
            return render(request, 'main/index.html')
        else:
            print(new_message.error)

    if request.user.is_authenticated:
        name = request.user.userdetail.user_first_name + ' ' + \
               request.user.userdetail.user_last_name
        email = request.user.email
        form = CustomerMessageForm(initial={
          'customer_name': name,
          'customer_email': email,
          })
    else:
        form = CustomerMessageForm()
    context = {'form': form}
    template = 'main/contact_us.html'
    return render(request, template, context)


def home(request):
    '''
    Renders Landing Page
    **Context**
    ```products```
    Three specific instances of :model:`product.Product`
    **Template**
        :template:`main/index.html`
    '''
    template = 'main/index.html'
    product_ids = [10, 31, 32]
    products = Product.objects.filter(id__in=product_ids).order_by('id')
    context = {'products': products}
    return render(request, template, context)


def privacy_policy(request):
    '''
    Renders Privacy Policy Page
    **Template**
        :template:`main/privacy_policy.html`
    '''
    request.session['newsletter_shown'] = False
    template = 'main/privacy_policy.html'
    context = {}
    return render(request, template, context)


def terms_and_conditions(request):
    '''
    Renders Terms and Conditions Page
    **Template**
        :template:`main/terms_and_conditions.html`
    '''
    template = 'main/terms_and_conditions.html'
    context = {}
    return render(request, template, context)


def verify_email(request, token):
    '''
    This view is called when a customer clicks a verification link on a
    received email, with which to verify their email address. The view
    receives a generated token (instantiated in the newsletter_signup
    view below) with which to check for validation. If valid, a new
    instance of :model:'main.DiscountCode' is generated,
    saved, and emailed to the customer
    **Template**
        :template:`main/newsletter_signup_verified.html`
    '''
    check_token = NewsLetterSignup.objects.filter(token=token).first()
    check_token.is_verified = True
    check_token.save()

    # Create New Discount Code
    letters = [i for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    numbers = [i for i in '0123456789']
    new_discount_code = ''
    for i in range(2):
        new_discount_code += random.choice(letters)
        new_discount_code += random.choice(letters)
        new_discount_code += random.choice(numbers)
    code_to_save = DiscountCode(
        discount_code=new_discount_code
    )
    code_to_save.save()

    # Send Customer newly created Discount Code
    subject = 'Your Discount Code for Heritage Company'
    message = render_to_string(
        'main/newsletter/email_discount_code_body.html',
        {'code': code_to_save.discount_code})

    send_mail(
        subject=subject,
        html_message=message,
        message='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[check_token.customer_email],
        )

    return render(request, 'main/newsletter_signup_verified.html')


def newsletter_signup(request):
    '''
    This view is called when a customer signs up for the
    site newsletter. It generates a new instance of
    :form:`main.NewsLetterSignupsForm`. It also generates a
    verification link (which includes the uuid token) in
    :model:`main.NewsLetterSignup`, and then emails the customer.
    **Context**
    ```email```
    The customers email address retrieved from the newly created
    instance of :model:`main.NewsLetterSignup`
    **Template**
        :template:`main/newsletter_signup.html`
    '''
    if request.method == 'POST':

        new_email = request.POST.get('customer_email')
        if NewsLetterSignup.objects.filter(customer_email=new_email).exists():
            return render(request, 'main/newsletter_error.html')

        new_signup = NewsLetterSignupsForm(data=request.POST)
        if new_signup.is_valid():
            client = new_signup.save()
        else:
            print(new_signup.errors)

        # Send Verification Email

        verification_link = reverse('verify_email', args=[client.token])
        verification_url = f"{settings.SITE_URL}{verification_link}"
        subject = 'Please Verify your email'
        message = render_to_string(
            'main/newsletter/email_signup_body.html',
            {'link': verification_url})

        send_mail(
            subject=subject,
            html_message=message,
            message='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[client.customer_email],
            )

        template = 'main/newsletter_signup.html'
        context = {'email': client.customer_email}
        return render(request, template, context)

    return render(request, 'main/index.html')


def newsletter_shown(request):
    '''
    This view is called when the customer has scrolled
    down far enough on the landing page (or other pages), and the
    newsletter signup modal has been displayed. It updates
    the Django backend session variable to avoid the newsletter
    being displayed again. Details in /static/assets/js/project.js
    **Context**
        None - JsonResponse with status and message
    '''
    if request.method == 'POST':
        data = json.load(request)
        request.session['newsletter_shown'] = data['newsletterShown']

        return JsonResponse({
          'status': 'ok',
          'message': 'Newsletter Shown Noted'
          })
