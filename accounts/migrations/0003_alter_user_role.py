# Generated by Django 4.1.3 on 2023-01-07 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_user_phone_number_userprofile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Restaurante'), (2, 'Cliente')], null=True, verbose_name='Rol'),
        ),
    ]
