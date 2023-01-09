from django.urls import path
from .views import *
from accounts.views import vendorDashboard


urlpatterns = [
    path('', vendorDashboard, name='vendor'),
    path('profile/', vProfile, name='v_profile'),
]