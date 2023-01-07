from django.urls import path
from .views import *


urlpatterns = [
    path('register-user/', registerUser, name='register_user'),
    path('register-vendor/', registerVendor, name='register_vendor'),

    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
]