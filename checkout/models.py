from django.db import models
from product.models import Product
from django_countries.fields import CountryField
from django.contrib.auth.models import User


class CheckoutSingleItem(models.Model):
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
    city = models.CharField(max_length=254, null=True, blank=True)
    postcode = models.CharField(max_length=254, null=True, blank=True)
    country = CountryField(null=True, blank=True)
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
        return text_data
