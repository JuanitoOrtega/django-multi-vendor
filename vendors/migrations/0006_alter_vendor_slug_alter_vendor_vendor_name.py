# Generated by Django 4.1.3 on 2023-01-13 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0005_vendor_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='slug',
            field=models.SlugField(max_length=150, unique=True, verbose_name='URL amigable'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vendor_name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Nombre del vendedor'),
        ),
    ]
