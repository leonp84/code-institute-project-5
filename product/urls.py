from django.urls import path
from . import views

urlpatterns = [
    path('all_products/', views.all_products, name='all_products'),
    path('product_detail/<int:product_id>',
         views.product_detail, name='product_detail'),
]
