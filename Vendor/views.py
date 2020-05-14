from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from .forms import MenuModel
from .models import Menu
from django.shortcuts import get_object_or_404
# Create your views here.
def index(request):
    food=Menu.objects.all()
    context={'foods':food}
    return render(request, 'index.html',context)

def menu(request):

    return render(request, 'reservation.html')



class MenuDetail(DetailView):
      model = Menu
      template_name='detail.html'

      def get(self, request, *args, **kwargs):
        book = get_object_or_404(Menu, pk=kwargs['pk'])
        context = {'food': book}
        return render(request, 'detail.html', context)


    
        

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


    