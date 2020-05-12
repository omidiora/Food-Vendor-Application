from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .forms import MenuModel
from .models import Menu
# Create your views here.
def index(request):
    return render(request, 'index.html')

def menu(request):

    return render(request, 'reservation.html')
    

class MenuView(CreateView):
    model=Menu
    fields=['name','description','price','quantity',]
    template_name='menu.html'
    success_url = '/'


#Edit View and update View
class MenuUpdate(UpdateView):
    model = Menu
    fields = ['name','description','price','quantity',]
    template_name = 'menu_update_form.html'
    success_url = '/'

    