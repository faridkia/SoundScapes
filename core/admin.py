from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


# Register your models here.


# @admin.register(Ticket)
# class TicketAdmin(admin.ModelAdmin):
#     list_display = ['user', 'subject', 'solved']
#     list_editable = ['solved']
#     list_filter = ['solved']
#
# @admin.register(Like)
# class LikeAdmin(admin.ModelAdmin):
#     list_display = ['user', 'song']

#TODO:SEARCH FIELD EZAFE BESHE

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['name','artists', 'subject', 'genre', 'listen_count']
    list_filter = ['artists', 'genre']


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'hide']
    list_editable = ['hide']

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['title']


