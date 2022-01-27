from pyexpat import model
from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import RedirectView, ListView, UpdateView, DeleteView, FormView, DetailView
from django.contrib.auth import logout as auth_logout, login
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from .filters import PlantFilter
import requests
from requests_html import HTMLSession
import urllib


# Create your views here.


class Login(LoginView):
    template_name = 'login.html'
    fields = ['username', 'password']
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard')


# class LandingPageView(TemplateView):

#     template_name = 'base/index.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['myfilter'] = PlantFilter()
#         return context

class LandingPageView(ListView):

    template_name = 'base/index.html'
    model = Plant

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(name__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list


class aboutPageView(TemplateView):
    template_name = 'base/about.html'


class contactPageView(TemplateView):
    template_name = 'base/contact.html'


class LogoutView(RedirectView):

    """
    Provides users the ability to logout
    """

    url = '/login/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class AdminDashboard(LoginRequiredMixin, ListView):
    """
        if login user not logged in redirect to login_url
    """

    login_url = '/login/'

    model = Plant
    template_name = 'admin.html'
    context_object_name = 'plants'


class EditPlant(LoginRequiredMixin, UpdateView):
    model = Plant
    form_class = PlantForm
    template_name = 'edit.html'
    success_url = '/dashboard/'


class DeletePlant(LoginRequiredMixin, DeleteView):
    model = Plant
    success_url = reverse_lazy('dashboard')


class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    # redirect_authenticated_user = True
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)


class CreatePlant(FormView):
    template_name = 'createplant.html'
    form_class = PlantForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = form.save()
        return super(CreatePlant, self).form_valid(form)


def ScrapeView(request):
    context = {}
    if request.method == 'POST':
        try:
            session = HTMLSession()
            response = session.get(
                "https://pubmed.ncbi.nlm.nih.gov/?term=" + request.POST.get('search'))

        except requests.exceptions.RequestException as e:
            print(e)
        else:
            links = response.html.absolute_links
            context['links'] = links
            print(links)
    return render(request, 'scrape.html', context)
