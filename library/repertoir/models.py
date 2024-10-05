from django.db import models

class Repertoir(models.Model):
    title = models.CharField('title', max_length=400)
    text = models.CharField('text', max_length=1500)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Repertoir'
        verbose_name_plural = 'Repertoirs'