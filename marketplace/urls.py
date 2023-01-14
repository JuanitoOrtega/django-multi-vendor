from django.urls import path
from .views import *


urlpatterns = [
    path('', marketplace, name='marketplace'),
    path('<slug:slug>/', vendorDetail, name='vendor_detail'),
]