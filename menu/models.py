from django.db import models
from vendors.models import Vendor


class Category(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, verbose_name='Vendedor')
    category_name = models.CharField(max_length=50, unique=True, verbose_name='Categoría')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL amigable')
    description = models.TextField(max_length=250, blank=True, verbose_name='Descripción')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def clean(self):
        self.category_name = self.category_name.capitalize()
    
    def __str__(self):
        return self.category_name


class FoodItem(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, verbose_name='Vendedor')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoría')
    food_title = models.CharField(max_length=50, unique=True, verbose_name='Título del plato')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL amigable')
    description = models.TextField(max_length=250, blank=True, verbose_name='Descripción')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    image = models.ImageField(upload_to='foodimages', verbose_name='Imagen')
    is_available = models.BooleanField(default=True, verbose_name='Disponible')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Menú'
        verbose_name_plural = 'Menús'

    def clean(self):
        self.food_title = self.food_title.capitalize()

    def __str__(self):
        return self.food_title