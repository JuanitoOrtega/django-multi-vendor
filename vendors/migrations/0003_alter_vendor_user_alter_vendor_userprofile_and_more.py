# Generated by Django 4.1.3 on 2023-01-07 04:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_user_phone_number_userprofile_phone_number'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendors', '0002_remove_vendor_userprofile_vendor_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='userprofile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to='accounts.userprofile', verbose_name='Perfil de usuario'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vendor_name',
            field=models.CharField(max_length=50, verbose_name='Nombre del vendedor'),
        ),
    ]
