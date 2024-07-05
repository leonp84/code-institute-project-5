from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    '''
    Created a form instance of :model:`checkout.Order`
    '''
    class Meta:
        model = Order
        fields = '__all__'
