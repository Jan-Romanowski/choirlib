from django.db import models
from django.utils import timezone

class Folder(models.Model):

    name = models.CharField('name', max_length=45, unique=True)
    note = models.CharField('note', max_length=250, null=True, blank=True) # Может быть нулём + можно ничего не вписывать в форме
    colour = models.CharField('colour', max_length=25, null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Folder'
        verbose_name_plural = 'Folders'
