from django.db import models


class Composition(models.Model):
    name = models.CharField('name', max_length=45)
    author = models.CharField('author', max_length=35)
    folder = models.CharField('folder', max_length=10)
    note = models.CharField('note', max_length=250)
    createDate = models.DateTimeField('createDate')
    changeDate = models.DateTimeField('changeDate')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
