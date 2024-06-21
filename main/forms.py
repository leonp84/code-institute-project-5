from django import forms
from .models import NewsLetterSignup


class NewsLetterSignupsForm(forms.ModelForm):
    class Meta:
        model = NewsLetterSignup
        fields = ('customer_email',)
