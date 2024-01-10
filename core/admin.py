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

#TODO:SEARCH FIELD EZAFE BESHE, Inline

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['name','artist', 'genre', 'listen_count']
    list_filter = ['artist', 'genre']
    # prepopulated_fields = {'slug': ('artist','name')}

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'hide']
    list_editable = ['hide']
    # prepopulated_fields = {'slug': ('user', 'title')}

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug':  ('name',)}


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(FavoriteSong)
class FavoriteSongAdmin(admin.ModelAdmin):
    list_display = ['user','song']


@admin.register(FavoritePlaylist)
class FavoritePlaylistAdmin(admin.ModelAdmin):
    list_display = ['user','playlist']

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ['follower','following']
