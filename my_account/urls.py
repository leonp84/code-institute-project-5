from django.urls import path
from . import views

urlpatterns = [
    path('my_account/', views.my_account, name='my_account'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('check_discount_code/', 
         views.check_discount_code, name='check_discount_code'),
    path('add_bookmarked_item/',
         views.add_bookmarked_item, name='add_bookmarked_item'),
]
