from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django_countries.fields import CountryField
# from django.contrib.gis.db import models as gismodels
# from django.contrib.gis.geos import Point


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('El registro debe tener un correo electrónico')

        if not username:
            raise ValueError('El registro debe tener un nombre de usuario')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    VENDOR = 1
    CUSTOMER = 2

    ROLE_CHOICE = (
        (VENDOR, 'Vendedor'),
        (CUSTOMER, 'Cliente'),
    )
    first_name = models.CharField(max_length=50, verbose_name='Nombres')
    last_name = models.CharField(max_length=50, verbose_name='Apellidos')
    username = models.CharField(max_length=50, unique=True, verbose_name='Usuario')
    email = models.EmailField(max_length=100, unique=True, verbose_name='Correo electrónico')
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True, verbose_name='Rol')

    # required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False, verbose_name='Activo')
    is_superadmin = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def get_role(self):
        # user_role = None
        if self.role == 1:
            user_role = 'Vendedor'
        elif self.role == 2:
            user_role = 'Cliente'
        return user_role

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Usuario')
    profile_picture = models.ImageField(upload_to='users/profile_pictures', blank=True, null=True, verbose_name='Foto de perfil')
    cover_photo = models.ImageField(upload_to='users/cover_photos', blank=True, null=True, verbose_name='Foto de portada')
    phone_number = models.CharField(max_length=12, blank=True, verbose_name='Número de teléfono')
    address = models.CharField(max_length=250, blank=True, null=True, verbose_name='Dirección')
    country = CountryField(blank_label='Seleccionar país', blank=True, null=True, verbose_name='País')
    state = models.CharField(max_length=50, blank=True, null=True, verbose_name='Estado/Departamento')
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name='Ciudad')
    pin_code = models.CharField(max_length=6, blank=True, null=True, verbose_name='Código PIN')
    latitude = models.CharField(max_length=20, blank=True, null=True, verbose_name='Latitud')
    longitude = models.CharField(max_length=20, blank=True, null=True, verbose_name='Longitud')
    # location = gismodels.PointField(blank=True, null=True, srid=4326, verbose_name='Ubicación')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')
    modified_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
    
    def full_address(self):
        if self.address:
            return '%s, %s, %s' % (self.address, self.city, self.state)
        else:
            return None

    # def save(self, *args, **kwargs):
    #     if self.latitude and self.longitude:
    #         self.location = Point(float(self.longitude), float(self.latitude))
    #         return super(UserProfile, self).save(*args, **kwargs)
    #     return super(UserProfile, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.user.email