from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    ordering = ['date_joined']
    add_fieldsets = (
        (None, {
        'classes': ('wide',),
        'fields': ('email', 'password1', 'password2'),
        }),
    )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    list_display = ('email', 'is_active', 'is_staff','is_superuser', 'date_joined',)
    search_fields = ('email',)
    ordering = ('date_joined',)
