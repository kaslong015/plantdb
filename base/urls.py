from django import urls
from django.urls import path
from .views import *

urlpatterns = [
    path('', LandingPageView.as_view(), name='index'),
    path('about/', aboutPageView.as_view(), name='about'),
    path('contact/', contactPageView.as_view(), name='contact'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', AdminDashboard.as_view(), name='dashboard'),
    path('edit/<slug:slug>/', EditPlant.as_view(), name='edit'),
    path('delete/<slug:slug>/', DeletePlant.as_view(), name="delete"),
    path('register/', RegisterPage.as_view(), name="register"),
    path('scrape/', ScrapeView, name="scrape"),
    path('create_plant',CreatePlant.as_view(), name="plant")
]
