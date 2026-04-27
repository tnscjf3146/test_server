from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('additional_profile', {'fields': ('nickname', 'profile_image', )})
    )

admin.site.register(User, CustomUserAdmin)