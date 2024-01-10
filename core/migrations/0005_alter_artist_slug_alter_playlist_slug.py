# Generated by Django 4.2.1 on 2024-01-06 15:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0004_alter_song_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="artist",
            name="slug",
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name="playlist",
            name="slug",
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
