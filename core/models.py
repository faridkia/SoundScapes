from django.db import models
from accounts.models import User
from django_resized import ResizedImageField
import math
from time import strftime, gmtime
from django.template.defaultfilters import slugify
from django.utils import timezone
import datetime

# class Ticket(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE, max_length=100)
#     message = models.TextField(max_length=300)
#     subject = models.CharField(max_length=250)
#     created = models.DateTimeField(auto_now_add=True)
#     solved = models.BooleanField(default=False)
#
#     class Meta:
#         ordering = ['created']
#         verbose_name = 'Ticket'
#         verbose_name_plural = 'Tickets'
#     def __str__(self):
#         return self.subject

#TODO:get absolute url to har kodom niaze ezafe beshe
class Genre(models.Model):
    title = models.CharField(max_length=20, unique=True)
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class FavoriteSong(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='favorite-songs')
    song = models.ForeignKey(Song, on_delete=models.PROTECT, related_name='favorites')

class FavoritePlaylist(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='favorite_playlists')
    playlist = models.ForeignKey(Playlist, on_delete=models.PROTECT, related_name='favorites')

class LikedSong(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='song_likes')
    song = models.ForeignKey(Song, on_delete=models.PROTECT, related_name='likes')
class LikedPlaylist(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='playlist_likes')
    playlist = models.ForeignKey(Playlist, on_delete=models.PROTECT, related_name='likes')

class Playlist(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')
    image = ResizedImageField(verbose_name='image', upload_to="playlists/images/",default='/accounts/static/img/default.png')
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)
    hide = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.slug = f'{slugify(self.user.username)}-{slugify(self.title)}'
        super(Artist, self).save(*args, **kwargs)


class Song(models.Model):
    name = models.CharField(max_length=50)
    image = ResizedImageField(upload_to='songs/images/', default='/accounts/static/img/musics.jpg')#dorost beshe
    audio = models.FileField(upload_to='songs/audios/')
    artist = models.ForeignKey('Artist', related_name='songs')
    slug = models.SlugField(unique=True)
    playtime = models.CharField(max_length=20, default="0.00")
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT, related_name='songs')
    playlists = models.ManyToManyField('Playlist', blank=True, related_name='songs')
    listen_count = models.BigIntegerField(default=0)
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['pk']

    def get_next_song(self): #linked-list
        return Song.objects.filter(pk__gt=self.id).order_by('pk').first()

    def get_previous_song(self):
        if self.id > 1:
            return Song.objects.filter(pk__lt=self.id).order_by('-pk').first()
        return None

    def __str__(self):
        return self.name

    @property
    def duration(self):
        return str(strftime('%H:%M:%S', gmtime(float(self.playtime))))

    def save(self, *args, **kwargs):
        self.slug = f'{slugify(self.artist)}-{slugify(self.name)}'
        super(Artist, self).save(*args, **kwargs)

class Artist(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="artists", default="/accounts/static/img/default.png")
    bio = models.TextField(verbose_name='Artist Bio', null=True, blank=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Artist, self).save(*args, **kwargs)