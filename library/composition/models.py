from django.db import models
from django.utils import timezone

class Composition(models.Model):
    name = models.CharField('name', max_length=45)
    author = models.CharField('author', max_length=35)
    number = models.CharField('number', max_length=5)
    folder = models.CharField('folder', max_length=10)
    isActual = models.BooleanField('isActual', default=False)
    note = models.CharField('note', max_length=250, null=True, blank=True) # Может быть нулём + можно ничего не вписывать в форме
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Composition'
        verbose_name_plural = 'Compositions'
