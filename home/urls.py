from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name = 'home'), #for homepage
    path('login/',views.LoginInterfaceView.as_view(), name = 'login'),
    path('logout/',views.logoutUser, name = 'logout')
] 