from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from product.models import Product


class UserDetail (models.Model):
    '''
    Stores user details for users that have created an account.
    These details can then later be used during the checkout process.
    A new instance of this model is automatically created via
    the post_save signal below, whenever (1) django Allauth creates
    a new user account or, (2) a new account is created in the checkout view)
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_first_name = models.CharField(
      max_length=254, null=True, blank=True, default="")
    user_last_name = models.CharField(
      max_length=254, null=True, blank=True, default="")
    user_phone_number = models.CharField(
      max_length=254, null=True, blank=True, default="")
    user_street_address1 = models.CharField(
      max_length=254, null=True, blank=True, default="")
    user_street_address2 = models.CharField(
      max_length=254, null=True, blank=True, default="")
    user_city = models.CharField(
      max_length=254, null=True, blank=True, default="")
    user_postcode = models.CharField(
      max_length=254, null=True, blank=True, default="")
    user_country = CountryField(
      null=True, blank=True, default="")
    user_delivery_notes = models.TextField(
      null=True, blank=True, default="")
    wish_list = models.ManyToManyField(Product)

    def __str__(self):
        return f"{self.user}'s User Details"


@receiver(post_save, sender=User)
def update_myaccount_profile(sender, instance, created, **kwargs):
    if created:
        UserDetail.objects.create(user=instance)
    else:
        instance.userdetail.save()
