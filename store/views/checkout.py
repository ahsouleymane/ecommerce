from django.shortcuts import render
from store.models import *
from store.utils import cartData

def checkout(request):
    
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems, 'shipping':False}
    return render(request, 'store/checkout.html', context)