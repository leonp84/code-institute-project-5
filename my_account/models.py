from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from product.models import Product


class UserDetail (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_first_name = models.CharField(
      max_length=254, null=True, blank=True)
    user_last_name = models.CharField(
      max_length=254, null=True, blank=True)
    user_phone_number = models.CharField(
      max_length=254, null=True, blank=True)
    user_street_address1 = models.CharField(
      max_length=254, null=True, blank=True)
    user_street_address2 = models.CharField(
      max_length=254, null=True, blank=True)
    user_city = models.CharField(
      max_length=254, null=True, blank=True)
    user_postcode = models.CharField(
      max_length=254, null=True, blank=True)
    user_country = CountryField(
      null=True, blank=True)
    user_delivery_notes = models.TextField(
      null=True, blank=True)
    wish_list = models.ManyToManyField(Product)

    def __str__(self):
        return f"{self.user}'s User Details"


@receiver(post_save, sender=User)
def update_myaccount_profile(sender, instance, created, **kwargs):
    if created:
        UserDetail.objects.create(user=instance)
    else:
        instance.userdetail.save()
