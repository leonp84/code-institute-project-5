from django.contrib import admin
from .models import CustomerMessage, NewsLetterSignup, DiscountCode

admin.site.register(CustomerMessage)


@admin.register(NewsLetterSignup)
class NewsLetterSignupAdmin(admin.ModelAdmin):
    list_display = ('customer_email', 'token', 'is_verified', 'sign_up_date',)


@admin.register(DiscountCode)
class DiscountCodeAdmin(admin.ModelAdmin):
    list_display = ('discount_code', 'date_created',)
    readonly_fields = ('discount_code',)
