from django.urls import path
from . import views # for views 

urlpatterns = [
    path('notes/', views.list),
]