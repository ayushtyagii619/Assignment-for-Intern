from django.db import models
class Course(models.Model):
    course_id = models.IntegerField(unique=True)
    course_name = models.CharField(max_length=255)
    course_provider=models.CharField(max_length=255)
    course_description = models.TextField()
    course_rating = models.CharField(max_length=255)
    course_language = models.CharField(max_length=255)
    course_duration=models.CharField(max_length=255)
    course_start_date = models.CharField(max_length=255)
    image_url = models.URLField()
    course_url = models.URLField()
    course_subject=models.CharField(max_length=255)
    course_topic = models.CharField(max_length=255)
    insert_timestamp= models.DateTimeField(auto_now_add=True)

# Create your models here.
