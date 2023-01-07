from django.contrib import admin
from .models import User, UserProfile
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    list_display = ['email', 'first_name', 'last_name', 'username', 'role', 'is_active']
    ordering = ['-date_joined']
    filter_horizontal = []
    list_filter = []
    fieldsets = []


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'country', 'state', 'city']
    ordering = ['-user']
    filter_horizontal = []
    list_filter = []
    fieldsets = []

    
admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)