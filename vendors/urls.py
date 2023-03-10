from django.urls import path
from .views import *
from accounts.views import vendorDashboard


urlpatterns = [
    path('', vendorDashboard, name='vendor'),
    path('profile/', vProfile, name='v_profile'),
    path('menu-builder/', menuBuilder, name='menu_builder'),
    path('menu-builder/category/<int:pk>/', foodItemsByCategory, name='fooditems_by_category'),

    # Category CRUD
    path('menu-builder/category/add/', addCategory, name='add_category'),
    path('menu-builder/category/edit/<int:pk>', editCategory, name='edit_category'),
    path('menu-builder/category/delete/<int:pk>', deleteCategory, name='delete_category'),

    # Food CRUD
    path('menu-builder/food/add/', addFoodItem, name='add_food'),
    path('menu-builder/food/edit/<int:pk>', editFoodItem, name='edit_food'),
    path('menu-builder/food/delete/<int:pk>', deleteFoodItem, name='delete_food'),
]