# Generated by Django 4.2.1 on 2024-01-04 21:49

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0004_alter_user_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="phone",
            field=models.CharField(
                blank=True,
                max_length=11,
                null=True,
                unique=True,
                verbose_name="Phone number",
            ),
        ),
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
