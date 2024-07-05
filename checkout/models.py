from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django_countries.fields import CountryField
from product.models import Product


class CheckoutSingleItem(models.Model):
    '''
    Stores an instance of a single item, and its quantities, that
    are in the customers shopping bag when they choose to checkout.
    NOTE: The fields `product_name_text` and `product_ref_text`
    specifically do NOT use foreignkey fields, but make text copies
    of the relevant information in :model:`product.Product` so that
    past order information is still available (and not blank) even
    when a product instance is deleted by a superuser.
    '''
    order_number = models.CharField(max_length=254)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    product_name_text = models.CharField(max_length=254)
    product_ref_text = models.CharField(max_length=254)
    product_price = models.IntegerField()
    quantity = models.IntegerField()

    def subtotal(self):
        return self.product_price * self.quantity

    def __str__(self):
        return f'Order: {self.order_number} of {self.product_name_text}'


class Order(models.Model):
    '''
    Stores an instance of a (paid) order after checkout. New instances
    of this model are created at checkout.views.order_confirmation.
    NOTE: The `items_ordered` & `items_ordered_admin` functions below
    return a HTML table element to display ordered products in both the
    my_account view (under 'past orders') or for superusers in the admin
    view (see checkout/admin.py)
    '''
    user = models.ForeignKey(
      User, on_delete=models.SET_NULL, null=True, blank=True)
    order_number = models.CharField(max_length=254)
    date_ordered = models.DateField(auto_now_add=True)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=254)
    street_address1 = models.CharField(max_length=254)
    street_address2 = models.CharField(max_length=254, blank=True)
    city = models.CharField(max_length=254)
    postcode = models.CharField(max_length=254)
    country = CountryField()
    delivery_notes = models.TextField(blank=True)
    order_total = models.IntegerField()
    watch_care_plan = models.BooleanField()
    grand_total = models.IntegerField()
    stripe_pid = models.CharField(max_length=254)

    def items_ordered(self):
        items = CheckoutSingleItem.objects.filter(
          order_number=self.order_number)
        text_data = "<table class='table'><tr><th>Product</th><th>Qty</th>\
                     <th>Price</th></tr>"
        for item in items:
            text_data += f"<tr><td class='small'>{item.product_name_text}</td>\
                           <td>{item.quantity}</td><td>${item.product_price:,}</td>\
                           </tr>"
        text_data += "</table>"
        return format_html(text_data)

    def items_ordered_admin(self):
        items = CheckoutSingleItem.objects.filter(
          order_number=self.order_number)
        text_data = "<table class='table'><tr><th>Product</th><th>Reference \
                     Number</th><th>Qty</th><th>Price</th></tr>"
        for item in items:
            text_data += f"<tr><td class='small'>{item.product_name_text}</td>\
                           <td>{item.product_ref_text}</td><td>{item.quantity}</td>\
                           <td>${item.product_price}</td>\
                           </tr>"
        text_data += "</table>"
        return format_html(text_data)

    def __str__(self):
        return self.order_number
