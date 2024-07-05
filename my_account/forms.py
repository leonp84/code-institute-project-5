from django import forms
from django.forms import Textarea
from django.utils.translation import gettext_lazy as _
from .models import UserDetail


class UserDetailsForm(forms.ModelForm):
    '''
    Creates a form instance of :model:`my_account.UserDetail` with custom
    labels, help texts and widgets for when logged in users choose to update
    their personal and delivery information.
    This form is used in my_account.views.update_profile and
    checkout.views.checkout
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = UserDetail
        exclude = ('user', 'wish_list',)
        labels = {
            "user_first_name": _("First Name"),
            "user_last_name": _("Last Name"),
            "user_phone_number": _("Phone Number"),
            "user_street_address1": _("Street Address"),
            "user_street_address2": _("Street Address 2"),
            "user_city": _("City"),
            "user_country": _("Country"),
            "user_postcode": _("Postcode"),
            "user_delivery_notes": _("Special Instructions"),
        }
        help_texts = {
            "user_phone_number": _("Please Enter your full phone number, \
                                    including the international country code"),
            "user_delivery_notes": _("Please include any special instructions \
                                      relating to your order. These may \
                                      pertain directly to Heritage Company, \
                                      or to the delivery company itself."),
        }
        required = {
            "user_first_name", "user_last_name", "user_phone_number",
            "user_street_address1", "user_city", "user_country",
            "user_postcode",
        }
        widgets = {
            "user_delivery_notes": Textarea(attrs={"cols": 80, "rows": 3}),
        }
