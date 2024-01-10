from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import *



@receiver(models.signals.pre_save, sender=Song)
def delete_file_on_change_photo(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_avatar = Song.objects.get(pk=instance.pk).image
        except Song.DoesNotExist:
            return
        else:
            new_avatar = instance.image
            if old_avatar and old_avatar.url != new_avatar.url:
                old_avatar.delete(save=False)

@receiver(models.signals.pre_save, sender=Playlist)
def delete_file_on_change_photo(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_avatar = Playlist.objects.get(pk=instance.pk).image
        except Playlist.DoesNotExist:
            return
        else:
            new_avatar = instance.image
            if old_avatar and old_avatar.url != new_avatar.url:
                old_avatar.delete(save=False)

@receiver(models.signals.pre_save, sender=Artist)
def delete_file_on_change_photo(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_avatar = Artist.objects.get(pk=instance.pk).image
        except Artist.DoesNotExist:
            return
        else:
            new_avatar = instance.image
            if old_avatar and old_avatar.url != new_avatar.url:
                old_avatar.delete(save=False)