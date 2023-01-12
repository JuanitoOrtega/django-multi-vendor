from django.forms import *
from .models import Category, FoodItem


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'description']
        # widgets = {
        #     'category_name': TextInput(
        #         attrs={
        #             'placeholder': 'Ingrese un nombre para la categoría',
        #         }
        #     ),
        #     'description': TextInput(
        #         attrs={
        #             'placeholder': 'Ingrese una descripción para la categoría',
        #         }
        #     )
        # }


class FoodItemForm(ModelForm):
    class Meta:
        model = FoodItem
        fields = ['category', 'food_title', 'description', 'price', 'image', 'is_available']
        widgets = {
            'food_title': TextInput(
                attrs={
                    'placeholder': 'Ej. Pizza Napolitana',
                }
            )
        }