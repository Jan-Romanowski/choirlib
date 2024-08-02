from django.db import models
from django.utils import timezone
from folder.models import Folder

class Composition(models.Model):
    name = models.CharField('name', max_length=45)
    author = models.CharField('author', max_length=35)
    number = models.PositiveIntegerField(unique=True)
    folder = models.ForeignKey(Folder, related_name='compositions', on_delete=models.SET_NULL, null=True, blank=True)
    isActual = models.BooleanField('isActual', default=False)
    note = models.CharField('note', max_length=250, null=True, blank=True) # Может быть нулём + можно ничего не вписывать в форме
    date_joined = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.number:
            # Генерация нового номера
            max_number = Composition.objects.all().order_by('-number').first()
            self.number = (max_number.number + 1) if max_number else 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Composition'
        verbose_name_plural = 'Compositions'
