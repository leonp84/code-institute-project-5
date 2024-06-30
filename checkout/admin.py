from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'date_ordered', 'user',
                    'items_ordered_admin', 'watch_care_plan', 'grand_total')

    def has_change_permission(self, request, obj=None):
        return False
