# Generated by Django 4.1.3 on 2023-01-13 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_alter_category_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='food_title',
            field=models.CharField(max_length=50, unique=True, verbose_name='Título del plato'),
        ),
    ]
