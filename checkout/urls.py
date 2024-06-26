from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('add_item_to_bag/', views.add_item_to_bag, name='add_item_to_bag'),
    path('update_shopping_bag/', 
         views.update_shopping_bag, name='update_shopping_bag'),
]
