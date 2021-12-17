from django.http import request
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView

# Create your views here.


class Login(LoginView):
    template_name = 'login.html'
    fields = ['username', 'password']
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')


class LandingPageView(TemplateView):
    template_name = 'base/index.html'


class aboutPageView(TemplateView):
    template_name = 'base/about.html'


class contactPageView(TemplateView):
   template_name = 'base/contact.html'
