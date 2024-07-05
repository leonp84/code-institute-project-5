from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    '''
    Custom order display in admin panel.
    NOTE: the 'items_ordered_admin' field below is a function of
    :model:`checkout.Order` that returns an HTML table element with
    information of purchased products displayed for superusers.
    '''
    list_display = ('order_number', 'date_ordered', 'user',
                    'items_ordered_admin', 'watch_care_plan', 'grand_total')

    def has_change_permission(self, request, obj=None):
        return False
