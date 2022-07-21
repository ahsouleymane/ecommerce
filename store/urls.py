from django.urls import path
from .views import store, cart, checkout, updateItem, processOrder

urlpatterns = [
    path('', store.store, name="store"),
    path('cart/', cart.cart, name="cart"),
    path('checkout/', checkout.checkout, name="checkout"),
    path('update_item/', updateItem.updateItem, name="update_item"),
    path('process_order/', processOrder.processOrder, name="process_order"),
]
