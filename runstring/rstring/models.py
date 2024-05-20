from django.db import models


class GeneratedVideo(models.Model):
    video_file = models.FileField(upload_to='videos/')
    created_at = models.DateTimeField(auto_now_add=True)
