from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


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


def newsletter_signup(request):
    if request.method == 'POST':
        new_signup_email = request.POST.get('email')

    subject = render_to_string(
        'main/newsletter/email_signup_subject.txt',
        {'order': "You didn't order a THING!"})
    body = render_to_string(
        'main/newsletter/email_signup_body.txt',
        {'contact_email': settings.DEFAULT_FROM_EMAIL})

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [new_signup_email]
        )

    template = 'main/newsletter_signup.html'
    context = {}
    return render(request, template, context)
