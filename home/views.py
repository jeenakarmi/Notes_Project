from django.shortcuts import render
from django.http import HttpResponse
from django .views.generic import TemplateView  #
from django.contrib.auth.mixins import LoginRequiredMixin # for login to authenticate


# Create your views here.
class HomeView(TemplateView):  #inherit from templateview
    #specifying home template that is used
    template_name = 'home/welcome.html'

class AuthorizedViews(LoginRequiredMixin ,TemplateView): # login before templateview
    template_name = 'home/authorized.html'
    login_url = '/admin/'           #login url

