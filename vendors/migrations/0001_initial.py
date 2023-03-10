# Generated by Django 4.1.3 on 2023-01-07 04:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_remove_user_phone_number_userprofile_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=50, verbose_name='Vendedor')),
                ('vendor_license', models.ImageField(blank=True, null=True, upload_to='vendor/license', verbose_name='Licencia')),
                ('is_approved', models.BooleanField(default=False, verbose_name='Aprobado')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
                ('userprofile', models.ManyToManyField(to='accounts.userprofile', verbose_name='Perfil de usuario')),
            ],
            options={
                'verbose_name': 'Vendedor',
                'verbose_name_plural': 'Vendedores',
            },
        ),
    ]
