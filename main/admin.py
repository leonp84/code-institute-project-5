from django.contrib import admin
from .models import CustomerMessage, NewsLetterSignup

admin.site.register(CustomerMessage)


@admin.register(NewsLetterSignup)
class NewsLetterSignupAdmin(admin.ModelAdmin):
    list_display = ('customer_email', 'token', 'is_verified', 'sign_up_date',)
