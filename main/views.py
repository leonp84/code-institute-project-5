from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from .forms import NewsLetterSignupsForm, CustomerMessageForm
from .models import NewsLetterSignup, DiscountCode
import random
import json


def about(request):
    template = 'main/about.html'
    context = {}
    return render(request, template, context)


def contact_us(request):

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
    template = 'main/index.html'
    context = {}
    return render(request, template, context)


def privacy_policy(request):
    request.session['newsletter_shown'] = False
    template = 'main/privacy_policy.html'
    context = {}
    return render(request, template, context)


def terms_and_conditions(request):
    template = 'main/terms_and_conditions.html'
    context = {}
    return render(request, template, context)


def verify_email(request, token):
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


def newsletter_shown(request):
    if request.method == 'POST':
        data = json.load(request)
        print('SEEN NEWSL = ' + str(data['newsletterShown']))
        request.session['newsletter_shown'] = data['newsletterShown']

        return JsonResponse({
          'status': 'ok',
          'message': 'Newsletter Shown Noted'
          })
