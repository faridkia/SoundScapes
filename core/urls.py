from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home,name='home'),
    path('dashboard/', views.dashboard,name='dashboard'),
    path('songs/', views.songs_list,name='songs'),
    path('songs/<slug:slug>', views.songs_detail,name='song-detail'),
    path('playlists/', views.playlist_list,name='playlists'),
    path('playlists/<slug:slug>', views.playlist_detail,name='playlist-detail'),
    path('favorite-song/<slug:slug>',views.make_song_favorite, name='mfavorites'),
    path('favorite-playlist/<slug:slug>',views.make_playlist_favorite, name='mfavoritep'),
    path('favorites/songs/', views.favorite_songs.as_view(),name='favorites-songs'),
    path('favorites/playlists/', views.favorite_playlists.as_view(),name='favorites-playlists'),
    path('profile/edit/', views.edit_profile, name='edit-profile'),
    path('profile/<str:username>', views.profile,name='profile'),
    path('users/', views.users_lists,name='users'),
    path('artists/', views.artists_list, name='artists'),
    path('artists/<slug:slug>', views.artist_detail,name='artist-details'),
    path('follow/<str:username>', views.follow_user, name='follow'),
]