# Generated by Django 4.1.3 on 2023-01-14 02:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('menu', '0007_alter_fooditem_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Cantidad')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
                ('fooditem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.fooditem', verbose_name='Ítems')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Carrito',
                'verbose_name_plural': 'Carritos',
            },
        ),
    ]
