from django import urls
from django.urls import path
from .views import *

urlpatterns = [
    path('', LandingPageView.as_view(), name='index'),
    path('about/', aboutPageView.as_view(), name='about'),
    path('contact/', contactPageView.as_view(), name='contact'),
    path('login/', Login.as_view(), name='login')
]
