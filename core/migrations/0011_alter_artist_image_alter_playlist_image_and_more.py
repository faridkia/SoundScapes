# Generated by Django 4.2.1 on 2024-01-06 16:17

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0010_alter_artist_image_alter_playlist_image_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="artist",
            name="image",
            field=django_resized.forms.ResizedImageField(
                crop=None,
                default="/accounts/static/img/default.png",
                force_format="JPEG",
                keep_meta=True,
                quality=100,
                scale=None,
                size=[400, 400],
                upload_to="artists",
            ),
        ),
        migrations.AlterField(
            model_name="playlist",
            name="image",
            field=django_resized.forms.ResizedImageField(
                crop=None,
                default="/accounts/static/img/default.png",
                force_format="JPEG",
                keep_meta=True,
                quality=100,
                scale=None,
                size=[400, 400],
                upload_to="playlists/images/",
                verbose_name="image",
            ),
        ),
        migrations.AlterField(
            model_name="song",
            name="image",
            field=django_resized.forms.ResizedImageField(
                crop=None,
                default="/accounts/static/img/musics.jpg",
                force_format="JPEG",
                keep_meta=True,
                quality=100,
                scale=None,
                size=[400, 400],
                upload_to="songs/images/",
            ),
        ),
    ]
