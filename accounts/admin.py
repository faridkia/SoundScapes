from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['username', 'phone','first_name', 'last_name']
    fieldsets = UserAdmin.fieldsets + (
        ('More Info', {'fields': ('date_of_birth', 'phone', 'photo')}),
    )


