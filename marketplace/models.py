from django.db import models
from accounts.models import User
from menu.models import FoodItem


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    fooditem = models.ForeignKey(FoodItem, on_delete=models.CASCADE, verbose_name='Ítems')
    quantity = models.PositiveIntegerField(verbose_name='Cantidad')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado')

    class Meta:
        verbose_name = 'Carrito'
        verbose_name_plural = 'Carritos'

    def __unicode__(self):
        return self.user


class Tax(models.Model):
    tax_type = models.CharField(max_length=20, unique=True, verbose_name='Tipo de impuesto')
    tax_percentage = models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Porcentaje de impuesto (%)')
    is_active = models.BooleanField(default=True, verbose_name='Activo')

    class Meta:
        verbose_name = 'Impuesto'
        verbose_name_plural = 'Impuestos'

    def __str__(self):
        return self.tax_type