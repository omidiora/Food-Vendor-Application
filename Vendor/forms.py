from django import forms
from django.forms import ModelForm
from .models import Menu

class MenuModel(ModelForm):
    class Meta:
        model=Menu
        fields=['name','description','price','quantity',]
    