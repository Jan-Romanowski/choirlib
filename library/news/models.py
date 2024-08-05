from django.db import models
from django.utils import timezone

class News(models.Model):

    title = models.CharField('title', max_length=200)
    text = models.CharField('text', max_length=3500)
    date_joined = models.DateTimeField(default=timezone.now)