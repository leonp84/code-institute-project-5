from django.urls import path
from . import views

urlpatterns = [
    path('all_products/', views.all_products, name='all_products'),
    path('breitling/', views.breitling, name='breitling'),
    path('tag_heuer/', views.tag_heuer, name='tag_heuer'),
    path('omega/', views.omega, name='omega'),
    path('tissot/', views.tissot, name='tissot'),
    path('search/', views.search, name='search'),
    path('advanced_search/', views.advanced_search, name='advanced_search'),
    path('sale/', views.sale, name='sale'),
    path('customer_product_message/',
         views.customer_product_message, name='customer_product_message'),
    path('product_detail/<int:product_id>',
         views.product_detail, name='product_detail'),
    path('add_new_product/', views.add_new_product, name='add_new_product'),
    path('edit_product/<int:product_id>', 
         views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>',
         views.delete_product, name='delete_product'),
]
