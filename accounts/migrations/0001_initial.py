# Generated by Django 4.1.3 on 2022-12-02 12:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(max_length=50, verbose_name='Nombres')),
                ('last_name', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='Usuario')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Correo electrónico')),
                ('phone_number', models.CharField(blank=True, max_length=12, verbose_name='Número de teléfono')),
                ('role', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Vendedor'), (2, 'Cliente')], null=True, verbose_name='Rol')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False, verbose_name='Activo')),
                ('is_superadmin', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='users/profile_pictures', verbose_name='Foto de perfil')),
                ('cover_photo', models.ImageField(blank=True, null=True, upload_to='users/cover_photos', verbose_name='Foto de portada')),
                ('address_line_1', models.CharField(blank=True, max_length=250, null=True, verbose_name='Dirección línea 1')),
                ('address_line_2', models.CharField(blank=True, max_length=250, null=True, verbose_name='Dirección línea 2')),
                ('country', models.CharField(blank=True, max_length=15, null=True, verbose_name='País')),
                ('state', models.CharField(blank=True, max_length=15, null=True, verbose_name='Estado/Departamento')),
                ('city', models.CharField(blank=True, max_length=15, null=True, verbose_name='Ciudad')),
                ('pin_code', models.CharField(blank=True, max_length=6, null=True, verbose_name='Código PIN')),
                ('latitude', models.CharField(blank=True, max_length=20, null=True, verbose_name='Latitud')),
                ('longitude', models.CharField(blank=True, max_length=20, null=True, verbose_name='Longitud')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfiles',
            },
        ),
    ]
