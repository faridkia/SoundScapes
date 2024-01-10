# Generated by Django 4.2.1 on 2024-01-06 16:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0007_alter_playlist_image_alter_song_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="song",
            name="playlists",
            field=models.ManyToManyField(
                blank=True, related_name="songs", to="core.playlist"
            ),
        ),
    ]
