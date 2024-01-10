# Generated by Django 4.2.1 on 2024-01-06 16:20

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0012_alter_user_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="photo",
            field=django_resized.forms.ResizedImageField(
                crop=None,
                default="user-profiles/user.jpg",
                force_format=None,
                keep_meta=True,
                quality=-1,
                scale=None,
                size=[1920, 1080],
                upload_to="user-profiles",
                verbose_name="Image",
            ),
        ),
    ]