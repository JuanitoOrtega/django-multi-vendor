# Generated by Django 4.1.3 on 2023-01-14 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_type', models.CharField(max_length=20, unique=True, verbose_name='Tipo de impuesto')),
                ('tax_percentage', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Porcentaje de impuesto (%)')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
            ],
            options={
                'verbose_name': 'Impuesto',
                'verbose_name_plural': 'Impuestos',
            },
        ),
    ]
