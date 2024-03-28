from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name = 'home'), #for homepage
    path('authorized/',views.AuthorizedViews.as_view(), name='authorized'), # for class based views for authentication
    path('login/',views.LoginInterfaceView.as_view())
]