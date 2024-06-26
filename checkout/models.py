from django.db import models
from product.models import Product


class CheckoutSingleItem(models.Model):
    bag_id = models.CharField(max_length=254)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    product_name_text = models.CharField(max_length=254)
    product_ref_text = models.CharField(max_length=254)
    product_price = models.IntegerField()
    quantity = models.IntegerField()

    def subtotal(self):
        return self.product_price * self.quantity
