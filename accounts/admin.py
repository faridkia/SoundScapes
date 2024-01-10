from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from core.models import *
# Register your models here.

class PlaylistInline(admin.TabularInline):
    model = Playlist
    extra = 1

@admin.register(User)
class UserAdmin(UserAdmin):
    inlines = [PlaylistInline]
    list_display = ['username', 'phone','first_name', 'last_name']
    fieldsets = UserAdmin.fieldsets + (
        ('More Info', {'fields': ('date_of_birth', 'phone', 'photo')}),
    )
    search_fields = ['username', 'phone']

