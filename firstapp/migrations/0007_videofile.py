# Generated by Django 4.2.16 on 2024-11-11 12:49

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ("firstapp", "0006_file"),
    ]

    operations = [
        migrations.CreateModel(
            name="VideoFile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=100, verbose_name="Описание файла"),
                ),
                (
                    "file",
                    models.FileField(upload_to="videos", verbose_name="Видеофайл"),
                ),
            ],
            managers=[
                ("obj_video", django.db.models.manager.Manager()),
            ],
        ),
    ]
