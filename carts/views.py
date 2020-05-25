from django.shortcuts import render
from .models import Cart
from Vendor.models import Menu

# Create your views here.
def cart_create(user=None):
    cart_obj=Cart.objects.create(user=None)
    print('New Cart created')
    return cart_obj



def home(request):
    # menu=Menu.objects.filter(name=request.user).first()
    # menus=Cart.objects.filter(user=request.user)
    # cart_id=request.session.get(menu,None)
    # qs=Cart.objects.filter(id=cart_id)
    # if qs.count()==1:
    #     new_obj=False
    #     cart_obj=qs.first()
    #     if request.user.is_authenticated and cart_obj.user is None:
    #         cart_obj.user=request.user
    #         cart_obj.save()
    

    # else:
    #     # cart_obj=cart_create()
    #     cart_obj=Cart.objects.create(user=request.user)
    #     request.session['cart_id']=cart_obj.id
  
    return render(request, 'checkout.html')

        
    
def checkout(request):
        menus=Menu.objects.filter(name=request.user).first()
        print(menus)


        context={'menus':menus}


        return render(request, 'checkout.html',context)

