from django.urls import path,include
from .views import *
from . import views


urlpatterns = [
    path('' , index , name='home'),
    path('food/<int:pk>' ,MenuDetail.as_view()  , name='home'),
    
    path('reservation' , menu, name='reservation'),
    path('menu/' ,  MenuView.as_view(), name='menu'),
    path('menuupdate/<pk>' ,   MenuUpdate.as_view(), name='menuupdate'),
   
]
    