from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_GET
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from itertools import chain
from django.contrib.postgres.search import TrigramSimilarity
from .forms import *
from datetime import datetime
from django.contrib import messages
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

#va gitignore

def home(request):
    if request.user.is_authenticated:
        return redirect('core:dashboard')
    return render(request, 'core/index.html')

@login_required
def dashboard(request):
    songs = Song.objects.all()[:4]
    playlists = Playlist.objects.all()[:4]
    artists = Artist.objects.all()[:4]
    return render(request, 'core/dashboard.html',{'songs' : songs, 'playlists':playlists, 'artists':artists})

@require_GET
def songs_list(request):
    search = request.GET.get('search')
    if search is None:
        songs = Song.objects.all().order_by('-listen_count')
    else:
        songs1 = Song.objects.annotate(similarity=TrigramSimilarity('name',search))\
            .filter(similarity__gt=0.1)
        songs2 = Song.objects.annotate(similarity=TrigramSimilarity('slug',search))\
            .filter(similarity__gt=0.1)
        songs = (songs1 | songs2).order_by('-similarity')
    paginator = Paginator(songs, 10)
    page = request.GET.get('page')

    try :
        songs = paginator.page(page)
    except PageNotAnInteger:
        songs = paginator.page(1)
    except EmptyPage:
        songs = paginator.page(paginator.num_pages)
    return render(request, 'core/songs.html',{'songs' : songs})

def songs_detail(request, slug):
    song = get_object_or_404(Song, slug=slug)
    song.listen_count += 1
    song.save()
    is_favorite = request.user.favorite_songs.filter(song=song).exists()
    return render(request, 'core/song_detail.html', {'song': song, 'is_favorite':is_favorite})

def playlist_list(request):
    search = request.GET.get('search')
    if search is None:
        playlists = Playlist.objects.all()
    else:
        playlist1 = Playlist.objects.annotate(similarity=TrigramSimilarity('title', search)) \
            .filter(similarity__gt=0.1)
        playlist2 = Playlist.objects.annotate(similarity=TrigramSimilarity('slug', search)) \
            .filter(similarity__gt=0.1)
        playlists = (playlist1 | playlist2).order_by('-similarity')
    paginator = Paginator(playlists, 6)
    page = request.GET.get('page')

    try:
        playlists = paginator.page(page)
    except PageNotAnInteger:
        playlists = paginator.page(1)
    except EmptyPage:
        playlists = paginator.page(paginator.num_pages)
    return render(request, 'core/playlists.html', {'playlists': playlists})

def artists_list(request):
    search = request.GET.get('search')
    if search is None:
        artists = Artist.objects.all()
    else:
        artist1 = Artist.objects.annotate(similarity=TrigramSimilarity('name', search)) \
            .filter(similarity__gt=0.1)
        artist2 = Artist.objects.annotate(similarity=TrigramSimilarity('slug', search)) \
            .filter(similarity__gt=0.1)
        artists = (artist1 | artist2).order_by('-similarity')
    paginator = Paginator(artists, 6)
    page = request.GET.get('page')

    try:
        artists = paginator.page(page)
    except PageNotAnInteger:
        artists = paginator.page(1)
    except EmptyPage:
        artists = paginator.page(paginator.num_pages)
    return render(request, 'core/artists.html', {'artists': artists})

def playlist_detail(request, slug):
    playlist = get_object_or_404(Playlist, slug=slug)
    is_favorite = request.user.favorite_playlists.filter(playlist=playlist).exists()
    return render(request, 'core/playlist-detail.html', {'playlist':playlist, 'is_favorite':is_favorite})


class favorite_songs(LoginRequiredMixin,ListView):
    model = User
    template_name = 'core/favorite_songs.html'
    context_object_name = 'songs'
    paginate_by = 10
    def get_queryset(self):
        return self.request.user.favorite_songs.all()
class favorite_playlists(LoginRequiredMixin,ListView):
    model = User
    template_name = 'core/favorite_playlists.html'
    context_object_name = 'playlists'
    paginate_by = 6
    def get_queryset(self):
        return self.request.user.favorite_playlists.all()

@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    songs = user.favorite_songs.all()[:3]
    playlists = user.favorite_playlists.all()[:3]
    today = datetime.now().date()
    is_followed = request.user.following.filter(following=user.id).exists()
    if user.date_of_birth :
        is_birthday = (user.date_of_birth.day == today.day and user.date_of_birth.month == today.month)
    else:
        is_birthday = False
    return render(request, 'core/profile.html', {'user':user, 'is_birthday':is_birthday, 'songs':songs, 'playlists':playlists,'is_followed':is_followed})

def artist_detail(request, slug):
    artist = get_object_or_404(Artist, slug=slug)
    return render(request, 'core/artist_detail.html', {'artist':artist})
@login_required
def edit_profile(request):
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile edited successfuly!', 'success')
            return redirect('core:edit-profile')
    else:
        form = EditProfileForm(instance=user)
    return render(request, 'core/edit_profile.html', {'form': form})
@login_required
def make_song_favorite(request, slug):
    song = get_object_or_404(Song, slug=slug)
    existing_favorite = FavoriteSong.objects.filter(user=request.user, song=song).exists()
    if not existing_favorite:
        FavoriteSong.objects.create(user=request.user, song=song)
    else:
        favorite = FavoriteSong.objects.get(user=request.user,song=song)
        favorite.delete()
    return redirect('core:song-detail',song.slug)

@login_required()
def make_playlist_favorite(request, slug):
    playlist = get_object_or_404(Playlist, slug=slug)
    existing_favorite = FavoritePlaylist.objects.filter(user=request.user, playlist=playlist).exists()
    if not existing_favorite:
        FavoritePlaylist.objects.create(user=request.user, playlist=playlist)
    else:
        favorite = FavoritePlaylist.objects.get(user=request.user,playlist=playlist)
        favorite.delete()
    return redirect('core:playlist-detail', playlist.slug)

@login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(User, username=username)

    existing_follow = Follow.objects.filter(follower=request.user, following=user_to_follow).exists()
    if not existing_follow:
        Follow.objects.create(follower=request.user, following=user_to_follow)
    else:
        follow = Follow.objects.get(follower=request.user, following=user_to_follow)
        follow.delete()
    return redirect('core:profile', user_to_follow.username)
@login_required()
def users_lists(request):
    search = request.GET.get('search')
    if search is None:
        users = User.objects.all()
    else:
        user1 = User.objects.annotate(similarity=TrigramSimilarity('username', search)) \
            .filter(similarity__gt=0.1)
        user2 = User.objects.annotate(similarity=TrigramSimilarity('first_name', search)) \
            .filter(similarity__gt=0.1)
        users = (user1 | user2).order_by('-similarity')
    paginator = Paginator(users, 10)
    page = request.GET.get('page')

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'core/users.html', {'users': users})

from django.core.mail import send_mail

#Not Used AnyMore But Maybe Functional In Next Update -- >
# @login_required
# def my_playlists(request):
#     playlists = request.user.playlists
#     favorite_playlists = FavoritePlaylist.objects.filter(user=user)
#     return render(request, ..., {'your_playlists': playlists, 'favorite_playlists': favorite_playlists})

# @login_required
# def favorite_songs(request):
#     songs = request.user.favorite_songs.all()
#     return render(request, 'core/favorite_songs.html', {'songs':songs})

# @login_required
# def favorite_playlists(request):
#     playlists = request.user.favorite_playlists.all()
#     return render(request, 'core/favorite_playlists.html', {'playlists':playlists})
# def send_test_email(request):
#     send_mail(
#         'SoundScapes Buff',
#         'Start your month with SoundScapes music platform to have better mood 😉💕!',
#         'soundscapesinfo2@gmail.com',
#         ['omid.farid.ok@gmail.com'],
#         fail_silently=False,
#     )
#     return HttpResponse('Email sent successfully!')