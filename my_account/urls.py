from django.urls import path
from . import views

urlpatterns = [
    path('my_account/', views.my_account, name='my_account'),
    path('update_profile/', views.update_profile, name='update_profile'),
]
