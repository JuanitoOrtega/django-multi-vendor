from django.forms import *
from .models import User


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
            'email': TextInput(
                attrs={
                    'type': 'email',
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