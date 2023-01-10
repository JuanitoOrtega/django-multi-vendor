from django.forms import *
from .models import Vendor
from accounts.validators import allow_only_images_validator


class VendorForm(ModelForm):
    vendor_license = FileField(widget=FileInput(attrs={'class': 'btn btn-info'}), validators=[allow_only_images_validator])
    class Meta:
        model = Vendor
        fields = ['vendor_name', 'vendor_license']
        widgets = {
            'vendor_name': TextInput(
                attrs={
                    'class': 'foodbakery-dev-req-field',
                    'placeholder': 'Ej. Pizza Hut',
                }
            )
        }