from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=254)
    ref = models.CharField(max_length=254)
    desc = models.TextField()
    watch_brand = models.CharField(max_length=50)
    watch_gender = models.CharField(max_length=6)
    watch_case_size = models.IntegerField()
    watch_material = models.CharField(max_length=20)
    watch_dial_colour = models.CharField(max_length=20)
    price = models.IntegerField()
    image = models.ImageField(null=True, blank=True)

    def short_title(self):
        words = self.title.split()
        return words[0] if words else ''

    def __str__(self):
        return f"{self.watch_brand} {self.title}"