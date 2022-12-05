from django.urls import path
from .views import registerUser


urlpatterns = [
    path('registeruser/', registerUser, name='registeruser')
]