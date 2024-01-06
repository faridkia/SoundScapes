# Generated by Django 4.2.1 on 2024-01-02 22:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_alter_user_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="photo",
            field=models.ImageField(
                blank=True, null=True, upload_to="user-profiles", verbose_name="Image"
            ),
        ),
    ]