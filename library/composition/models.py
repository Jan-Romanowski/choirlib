from django.db import models
from django.utils import timezone

class Composition(models.Model):
    number = models.CharField('number', max_length=5)
    name = models.CharField('name', max_length=45)
    author = models.CharField('author', max_length=35)
    folder = models.CharField('folder', max_length=10)
    note = models.CharField('note', max_length=250)
    date_joined = models.DateTimeField(default=timezone.now)
    changeDate = models.DateTimeField('changeDate')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Composition'
        verbose_name_plural = 'Compositions'
