from django.db import models

# Create your models here.

class Diary(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)

