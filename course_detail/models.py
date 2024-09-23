from django.db import models

class Video(models.Model):
    video_id = models.CharField(max_length=10,unique=True)
    video_title = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    date_of_publish = models.CharField(max_length=255)
    youtube_url = models.URLField()
    time_of_additon = models.DateTimeField()

    

# Create your models here.
