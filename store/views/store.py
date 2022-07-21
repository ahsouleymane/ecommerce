from itertools import product
from django.shortcuts import render
from store.models import *
from store.utils import cartData

def store(request):
    
    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems, 'shipping':False}
    return render(request, 'store/store.html', context)