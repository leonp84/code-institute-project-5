from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
          'watch_brand',
          'title',
          'ref',
          'desc',
          'watch_gender',
          'watch_case_size',
          'watch_material',
          'watch_dial_colour',
          'discount_percentage',
          'price',)
