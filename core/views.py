from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from itertools import chain
# Create your views here.

#TODO:LOGIN REQUIRED HA, METHOD HA , TEMPLATE HA, 404 ERROR TEMPLATE, VIEW HOME

def hichi(request): #avas beshe
    return render(request, 'core/home.html')

@require_GET
def songs_list(request):
    songs = Song.objects.all()
    items_per_page = 10
    paginator = (songs, items_per_page)
    page = request.GET.get('page')

    try :
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    return render(request,...,{'songs' : items})

def songs_detail(request, slug):
    song = get_object_or_404(Song, slug=slug)
    return render(request, '...', {'song': song})

def playlist_list(request):
    playlists = Playlist.objects.all()
    items_per_page = 6
    paginator = (playlists, items_per_page)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    return render(request, ..., {'playlists': items})

def playlist_detail(request, slug):
    playlist = get_object_or_404(Playlist, slug=slug)
    return render(request, ..., {'playlist':playlist})

@login_required
def my_playlists(request):
    playlists = request.user.playlists
    favorite_playlists = FavoritePlaylist.objects.filter(user=user)
    return render(request, ..., {'your_playlists': playlists, 'favorite_playlists': favorite_playlists})

@login_required
def liked_songs(request):
    songs = request.user.song_likes
    return render(request, ..., {'songs':songs})

@login_required
def favorite_songs(request):
    songs = request.user.favorite_songs
    return render(request, ..., {'songs':songs})

@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, '', {'user':user})

def artist_detail(request, slug):
    artist = get_object_or_404(Artist, slug=slug)
    return render(request, '', {'artist':artist})
