from django.urls import path,include
from .views import *
from . import views


urlpatterns = [
    path('' , index , name='home'),
    path('reservation' , menu, name='home'),
    path('menu/' ,  MenuView.as_view(), name='home'),
    path('menuupdate/<pk>' ,   MenuUpdate.as_view(), name='home'),
   
]
    