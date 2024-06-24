from django import forms
from .models import Product
from django.forms import Textarea, TextInput, NumberInput
from django.utils.translation import gettext_lazy as _


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            "watch_brand": _("Brand Name"),
            "title": _("Watch Full Name"),
            "ref": _("Reference Number"),
            "desc": _("Watch Description"),
            "watch_gender": _("Gender"),
            "watch_case_size": _("Case Size in mm"),
            "watch_material": _("Case Material"),
            "watch_dial_colour": _("Dial Colour"),
            "discount_percentage": _("Discount Percentage"),
            "price": _("Price in US Dollars"),
            "image": _("Primary Display Image"),
            "image2": _("Secondary Image"),
            "image3": _("Tertiary Image"),
        }
        help_texts = {
            "title": _("The full watch title without brand name."),
            "desc": _("Recommended length: 50-100 words"),
            "watch_gender": _("Specify whether this is a male of female watch \
                               by typing 'M' or 'F'"),
            "discount_percentage": _("If the item is not on sale enter '0'"),
            "price": _("Enter only numbers without any commas or periods"),
            "image": _("The primary product image, ensure this is of high \
                        enough resolution and quality."),
        }
        widgets = {
            "desc": Textarea(attrs={"cols": 80, "rows": 3}),
            "title": TextInput(attrs={
              "placeholder": "ex. 'Carrera Heuer 02 Automatic Chronograph'"}),
            "ref": TextInput(attrs={"placeholder": "ex. 'A010589ZPO'"}),
            "watch_case_size": NumberInput(attrs={"placeholder": "44"}),
            "discount_percentage": NumberInput(),
            "price": NumberInput(),
            "watch_material": TextInput(attrs={
              "placeholder": "Stainless Steel"}),
            "watch_dial_colour": TextInput(attrs={"placeholder": "Blue"}),
        }
