from django.shortcuts import render,redirect
from django.http import HttpResponse
from django .views.generic import TemplateView,CreateView  #
from django.contrib.auth.mixins import LoginRequiredMixin # for login to authenticate

from django.contrib.auth.forms import UserCreationForm  #signup page

from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import logout
from . import views

# Create your views here.

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = 'smart/notes'

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

# class LogoutInterfaceView(LogoutView):
#     template_name = 'home/logout.html'

class HomeView(TemplateView):  #inherit from templateview
    #specifying home template that is used
    template_name = 'home/welcome.html'

def logoutUser(request):
    logout(request)
    return redirect ('/login')

