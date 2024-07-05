from django.db import models
import uuid


class CustomerMessage(models.Model):
    '''
    Stores an instance of a customer message which superusers can access
    in the admin panel (from the my_account page). New instances are created
    when customers send messages from main.views.contact_us, or from
    product.views.customer_product_message
    '''
    customer_name = models.CharField(max_length=254)
    customer_email = models.EmailField(max_length=254)
    product_name = models.CharField(max_length=254, blank=True)
    product_ref = models.CharField(max_length=254, blank=True)
    customer_message = models.TextField(blank=False)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name}: {self.customer_message}"


class NewsLetterSignup(models.Model):
    '''
    Stores an instance of a new newsletter subscriber. Instances of
    this model are available for viewing by superusers in the admin panel,
    accessible through the my_account view.
    '''
    customer_email = models.EmailField(max_length=254)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    is_verified = models.BooleanField(default=False)
    sign_up_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_email


class DiscountCode(models.Model):
    '''
    Stores an instance of a dynamically generated 6 digit discount code.
    Instances of this model is created at main.views.verify_email
    '''
    discount_code = models.CharField(max_length=6)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.discount_code
