from django.urls import path,include
from .views import *
from . import views


urlpatterns = [
    path('',home,name='carthome'),
    path('checkout/',checkout,name='checkout')
   
  
   
]
    