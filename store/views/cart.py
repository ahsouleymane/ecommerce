from django.shortcuts import render
from store.models import *

def cart(request):
    if request.user.is_authenticated:
        custumer = request.user.customer
        order, created = Order.objects.get_or_create(custumer, complete = False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items':items, 'order':order}
    return render(request, 'store/cart.html', context)