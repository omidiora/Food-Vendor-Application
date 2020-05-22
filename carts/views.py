from django.shortcuts import render
from .models import Cart

# Create your views here.
def cart_create(user=None):
    cart_obj=Cart.objects.create(user=None)
    print('New Cart created')
    return cart_obj



def home(request):
    cart_id=request.session.get('cart_id',None)
    qs=Cart.objects.filter(id=cart_id)
    if qs.count()==1:
            print('CArt id exitst')
            cart_obj=qs.first()
    else:
        cart_obj=cart_create()
        request.session['cart_id']=cart_obj.id
    return render(request, 'reservation.html')

        
    
    
