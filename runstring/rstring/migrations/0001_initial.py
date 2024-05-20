# Generated by Django 4.2.13 on 2024-05-19 18:03

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GeneratedVideo",
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
                ("video_file", models.FileField(upload_to="videos/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
