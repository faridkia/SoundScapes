from django.db import models
from accounts.models import User
from django_resized import ResizedImageField
import math
from django.urls import reverse
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

class Genre(models.Model):
    title = models.CharField(max_length=20, unique=True)
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class FavoriteSong(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='favorite_songs')
    song = models.ForeignKey('Song', on_delete=models.PROTECT, related_name='favorites')

    class Meta:
        unique_together = ('user', 'song')

class FavoritePlaylist(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='favorite_playlists')
    playlist = models.ForeignKey('Playlist', on_delete=models.PROTECT, related_name='favorites')

    class Meta:
        unique_together = ('user', 'playlist')

class LikedSong(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='song_likes')
    song = models.ForeignKey('Song', on_delete=models.PROTECT, related_name='likes')

    class Meta:
        unique_together = ('user', 'song')

class Playlist(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')
    image = ResizedImageField(verbose_name='image',size=[800, 800], force_format='JPEG',upload_to="playlists/images/",default='/accounts/static/img/default.png')
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)
    hide = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        combined_text = f'{self.user.username} {self.title}'
        self.slug = slugify(combined_text)
        super(Playlist, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('core:playlist-detail', args=[self.slug])


class Song(models.Model):
    name = models.CharField(max_length=50)
    image = ResizedImageField(upload_to='songs/images/',size=[800, 800], force_format='JPEG', default='/accounts/static/img/musics.jpg')
    audio = models.FileField(upload_to='songs/audios/')
    artist = models.ForeignKey('Artist',on_delete=models.PROTECT ,related_name='songs',default=1)
    slug = models.SlugField(unique=True,blank=True)
    playtime = models.CharField(max_length=20, default="0.00")
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT, related_name='songs', default=1)
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

    def play_music(self):
        # Simulate playing music
        self.listen_count += 1
        self.save()

    def __str__(self):
        return self.name

    @property
    def duration(self):
        return str(strftime('%H:%M:%S', gmtime(float(self.playtime))))

    def save(self, *args, **kwargs):
        combined_text = f'{self.artist} {self.name}'
        self.slug = slugify(combined_text)
        super(Song, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('core:song-detail', args=[self.slug])

class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')

class Artist(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True,blank=True)
    image = ResizedImageField(upload_to="artists",size=[800, 800],blank=True ,force_format='JPEG', default="artists/default.png")
    bio = models.TextField(verbose_name='Artist Bio', null=True, blank=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Artist, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('core:artists-detail', args=[self.slug])