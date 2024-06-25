from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('add_item_to_bag/', views.add_item_to_bag, name='add_item_to_bag'),
]
