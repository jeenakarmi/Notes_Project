from django.shortcuts import render
from django.http import HttpResponse
from django .views.generic import TemplateView  #
from django.contrib.auth.mixins import LoginRequiredMixin # for login to authenticate

from django.contrib.auth.views import LoginView


# Create your views here.

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

class LogoutInterfaceView(TemplateView):
    template_name = 'home/logout.html'

class HomeView(TemplateView):  #inherit from templateview
    #specifying home template that is used
    template_name = 'home/welcome.html'


