from django.urls import path
from . import views

urlpatterns = [
    path('',
         views.home, name='home'),
    path('about/',
         views.about, name='about'),
    path('newsletter_signup/',
         views.newsletter_signup, name='newsletter_signup'),
    path('privacy_policy/',
         views.privacy_policy, name='privacy_policy'),
    path('terms_and_conditions/',
         views.terms_and_conditions, name='terms_and_conditions'),
]
