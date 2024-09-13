from django.db import models

class Repertoir:
    title = models.CharField('title', max_length=550)
    text = models.CharField('text', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Repertoir'
        verbose_name_plural = 'Repertoirs'