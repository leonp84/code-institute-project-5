from django.db import models
import uuid


class CustomerMessage(models.Model):
    customer_name = models.CharField(max_length=254)
    customer_email = models.EmailField(max_length=254)
    product_name = models.CharField(max_length=254, blank=True)
    product_ref = models.CharField(max_length=254, blank=True)
    customer_message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name}: {self.customer_message}"


class NewsLetterSignup(models.Model):
    customer_email = models.EmailField(max_length=254)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    is_verified = models.BooleanField(default=False)
    sign_up_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_email


class DiscountCode(models.Model):
    discount_code = models.CharField(max_length=6)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.discount_code
