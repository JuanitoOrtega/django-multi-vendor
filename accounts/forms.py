from django.forms import *
from .models import User, UserProfile
from .validators import allow_only_images_validator


class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['first_name'].widget.attrs['autofocus'] = True

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        widgets = {
            'email': EmailInput(
                attrs={
                    'placeholder': '',
                }
            )
        }

    password = CharField(widget=PasswordInput())
    confirm_password = CharField(widget=PasswordInput())

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError('Las contraseñas ingresadas no coinciden')


class UserProfileForm(ModelForm):
    address = CharField(widget=TextInput(attrs={'placeholder': 'Comienza a escribir...', 'required': 'required'}))
    profile_picture = FileField(widget=FileInput(attrs={'class': 'btn btn-info'}), validators=[allow_only_images_validator])
    cover_photo = FileField(widget=FileInput(attrs={'class': 'btn btn-info'}), validators=[allow_only_images_validator])
    # cover_photo = ImageField(widget=FileInput(attrs={'class': 'btn btn-info'}), validators=[allow_only_images_validator])

    # latitude = CharField(widget=TextInput(attrs={'readonly': 'readonly'}))
    # longitude = CharField(widget=TextInput(attrs={'readonly': 'readonly'}))
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'cover_photo', 'address', 'country', 'state', 'city', 'pin_code', 'latitude', 'longitude']

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'latitude' or field == 'longitude':
                self.fields[field].widget.attrs['readonly'] = 'readonly'