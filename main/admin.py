from django.contrib import admin
from .models import CustomerMessage, NewsLetterSignup
from .models import DiscountCode


admin.site.site_header = "Heritage Company - Admin Panel"
admin.site.site_title = "Admin Panel"
admin.site.index_title = 'Heritage Company Dashboard'


@admin.register(NewsLetterSignup)
class NewsLetterSignupAdmin(admin.ModelAdmin):
    list_display = ('customer_email', 'token', 'is_verified', 'sign_up_date',)

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(DiscountCode)
class DiscountCodeAdmin(admin.ModelAdmin):
    list_display = ('discount_code', 'date_created',)
    readonly_fields = ('discount_code',)

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(CustomerMessage)
class CustomerMessageAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email', 'product_name',
                    'product_ref', 'date_sent', 'customer_message',)

    def has_change_permission(self, request, obj=None):
        return False
