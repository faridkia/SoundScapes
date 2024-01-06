from django.urls import path
from . import views

app_name = 'core'

#TODO:COMMENT HA BAD ETMAM KAR BARDASHTE BESHE
urlpatterns = [
    path('', views.hichi,name='home'),
    path('dashboard/', views.hichi,name='dashboard'),
    path('songs/', views.hichi(),name='songs'), #toosh search biad
    path('songs/<slug:slug>', views.hichi,name='songs'), #song detail
    path('playlists/', views.hichi,name='playlists'),
    path('playlists/<slug:slug>', views.hichi,name='playlists'),#playlist detail
    path('my-playlists/', views.hichi,name='playlists'), #che is favorite bood che khodesh sakhte bood biad
    path('favorites-songs/', views.hichi,name='favorites-songs'), #is favorite
    path('liked-songs/', views.hichi,name='favorites-songs'), # liked
    path('profile/<username>', views.hichi,name='favorites-songs'), # profile
    path('artists/<slug:slug>', views.hichi,name='favorites-songs'), # artist
]