from django.contrib import admin
from .models import Vendor


class VendorAdmin(admin.ModelAdmin):
    list_display = ['user', 'vendor_name', 'is_approved', 'created_at']
    list_display_links = ['user']
    # list_filter = ['is_approved']


admin.site.register(Vendor, VendorAdmin)