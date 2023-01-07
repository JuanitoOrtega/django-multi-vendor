from django.urls import path
from .views import registerUser, registerVendor


urlpatterns = [
    path('register-user/', registerUser, name='register_user'),
    path('register-vendor/', registerVendor, name='register_vendor'),
]