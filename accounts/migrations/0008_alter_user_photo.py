# Generated by Django 4.2.1 on 2024-01-06 16:00

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0007_alter_user_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="photo",
            field=django_resized.forms.ResizedImageField(
                crop=None,
                default="user.png",
                force_format="JPEG",
                keep_meta=True,
                quality=75,
                scale=0.5,
                size=[400, 400],
                upload_to="user-profiles",
                verbose_name="Image",
            ),
        ),
    ]