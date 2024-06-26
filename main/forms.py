from django import forms
from .models import NewsLetterSignup, CustomerMessage
from django.forms import Textarea
from django.utils.translation import gettext_lazy as _


class NewsLetterSignupsForm(forms.ModelForm):
    class Meta:
        model = NewsLetterSignup
        fields = ('customer_email',)


class CustomerMessageForm(forms.ModelForm):
    class Meta:
        model = CustomerMessage
        fields = ('customer_name', 'customer_email', 'customer_message',)
        labels = {
            "customer_name": _("Name"),
            "customer_email": _("Email"),
            "customer_message": _("Your Message:"),
        }
        widgets = {
            "customer_message": Textarea(attrs={"cols": 80, "rows": 3}),
        }
