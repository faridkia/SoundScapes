from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField
from django.dispatch import receiver
# Create your models here.

class User(AbstractUser):
    date_of_birth = models.DateField(verbose_name='Birth date', blank=True, null=True)
    photo = ResizedImageField(verbose_name='Image',upload_to="user-profiles", default='user.png')
    phone = models.CharField(max_length=11,verbose_name='Phone number',blank=True, null=True, unique=True)

@receiver(models.signals.pre_save, sender=User)
def delete_file_on_change_photo(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_avatar = User.objects.get(pk=instance.pk).photo
        except User.DoesNotExist:
            return
        else:
            new_avatar = instance.photo
            if old_avatar and old_avatar.url != new_avatar.url:
                old_avatar.delete(save=False)