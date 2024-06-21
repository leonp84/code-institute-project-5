from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string # noqa
from django.urls import reverse
from django.conf import settings
from .forms import NewsLetterSignupsForm
from .models import NewsLetterSignup


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


def verify_email(request, token):
    check_token = NewsLetterSignup.objects.filter(token=token).first()
    check_token.is_verified = True
    check_token.save()

    return HttpResponse('Thank you for verifying your email')


def newsletter_signup(request):
    if request.method == 'POST':
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
    context = {}
    return render(request, template, context)
