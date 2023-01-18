from django.urls import path
from .views import *


urlpatterns = [
    path('', marketplace, name='marketplace'),
    path('<slug:slug>/', vendorDetail, name='vendor_detail'),

    # Add to cart
    path('add-to-cart/<int:food_id>/', addToCart, name='add_to_cart'),
    # Decrease cart
    path('decrease-cart/<int:food_id>/', decreaseCart, name='decrease_cart'),
    # Delete cart item
    path('delete-cart/<int:cart_id>/', deleteCart, name='delete_cart'),
]