from django.db import models
from django.utils import timezone
from folder.models import Folder
import os

class Composition(models.Model):
    name = models.CharField('Name', max_length=45)
    author = models.CharField('Author', max_length=35)
    number = models.PositiveIntegerField(unique=True)
    folder = models.ForeignKey(Folder, related_name='compositions', on_delete=models.SET_NULL, null=True, blank=True)
    isActual = models.BooleanField('Is Actual', default=False)
    note = models.CharField('Note', max_length=250, null=True, blank=True)  # Может быть нулём + можно ничего не вписывать в форме
    date_joined = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.number:
            max_number = Composition.objects.all().order_by('-number').first()
            self.number = (max_number.number + 1) if max_number else 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Composition'
        verbose_name_plural = 'Compositions'


def composition_file_path(instance, filename):
    # Сохраняем файлы по пути: compositions/ID_произведения/имя_файла
    return os.path.join('compositions', str(instance.composition.id), filename)


class CompositionFile(models.Model):
    FILE_TYPES = [
        ('mp3', 'MP3 File'),
        ('wav', 'WAV File'),
        ('pdf', 'PDF File')
    ]

    composition = models.ForeignKey(Composition, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to=composition_file_path)
    file_type = models.CharField(max_length=3, choices=FILE_TYPES)

    def __str__(self):
        return f'{self.composition.name} - {self.get_file_type_display()}'
