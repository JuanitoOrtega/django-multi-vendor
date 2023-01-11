from django.forms import *
from .models import Category


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