from django.urls import path
from django.urls import re_path
from . import views
from . import stripe_webhooks


urlpatterns = [
    path('', views.shopping_bag, name='shopping_bag'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout_data/', views.checkout_data, name='checkout_data'),
    path('order_payment/', views.order_payment, name='order_payment'),
    re_path(r'^order_confirmation/?(?P<params>.*)$', views.order_confirmation,
            name='order_confirmation'),
    path('add_item_to_bag/', views.add_item_to_bag, name='add_item_to_bag'),
    path('update_watch_care_plan/',
         views.update_watch_care_plan, name='update_watch_care_plan'),
    path('update_shopping_bag/',
         views.update_shopping_bag, name='update_shopping_bag'),
    path('webhook/', stripe_webhooks.webhook, name='webhook'),
]
