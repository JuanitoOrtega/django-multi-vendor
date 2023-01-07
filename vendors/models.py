from django.db import models
from accounts.models import User, UserProfile


class Vendor(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE, verbose_name='Usuario')
    user_profile = models.OneToOneField(UserProfile, related_name='userprofile', on_delete=models.CASCADE, verbose_name='Perfil de usuario')
    vendor_name = models.CharField(max_length=50, verbose_name='Nombre del vendedor')
    vendor_license = models.ImageField(upload_to='vendor/license', blank=True, null=True, verbose_name='Licencia')
    is_approved = models.BooleanField(default=False, verbose_name='Aprobado')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Modificado')

    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'

    def __str__(self):
        return self.vendor_name