from django.contrib import admin
from .models import CheckoutSingleItem, Order

admin.site.register(CheckoutSingleItem)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'date_ordered', 'user', 'items_ordered',)
