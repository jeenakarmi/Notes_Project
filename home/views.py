from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django .views.generic import TemplateView  #

# Create your views here.
class HomeView(TemplateView):  #inherit from templateview
    #specifying home template that is used
    template_name = 'home/welcome.html'

@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'home/authorized.html', {} )