from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):

    class WatchBrand(models.TextChoices):
        BREITLING = "BR", _("Breitling")
        TAGHEUER = "TA", _("Tag Heuer")
        OMEGA = "OM", _("Omega")
        TISSOT = "TI", _("Tissot")

    class WatchGender(models.TextChoices):
        MALE = "M", ("Men's Watch"),
        FEMALE = "F", ("Women's Watch")
        UNISEX = "X", ("Unisex Watch")

    watch_brand = models.CharField(max_length=2, choices=WatchBrand)
    title = models.CharField(max_length=254)
    ref = models.CharField(max_length=254)
    desc = models.TextField()
    watch_gender = models.CharField(max_length=1, choices=WatchGender)
    watch_case_size = models.IntegerField()
    watch_material = models.CharField(max_length=50)
    watch_dial_colour = models.CharField(max_length=20)
    discount_percentage = models.IntegerField(default=0)
    price = models.IntegerField()
    image = models.ImageField(blank=False)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)

    def pre_discount_price(self):
        return int(self.price / (100 - self.discount_percentage) * 100)

    def short_title(self):
        words = self.title.split()
        return words[0] if words else ''

    def __str__(self):
        return f"{self.watch_brand} {self.title}"
