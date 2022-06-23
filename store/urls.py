from django.urls import path
from .views import store, cart, checkout

urlpatterns = [
    path('', store.store, name="store"),
    path('cart/', cart.cart, name="cart"),
    path('checkout/', checkout.checkout, name="checkout"),
]
