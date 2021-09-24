from m2m.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_autor')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'phone', 'is_autor')}),
        (_('favorites'), {'fields': ('favorites',)}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
