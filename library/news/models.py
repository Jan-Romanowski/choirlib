from django.db import models
from django.utils import timezone
import os

class News(models.Model):

    title = models.CharField('title', max_length=200)
    text = models.CharField('text', max_length=3500)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

def news_file_path(instance, filename):
    # Сохраняем файлы по пути: compositions/ID_произведения/имя_файла
    return os.path.join('compositions', str(instance.composition.id), filename)


class NewsFile(models.Model):
    FILE_TYPES = [
        ('png', 'PNG File'),
        ('jpg', 'JPG File'),
        ('jpeg', 'JPEG File')
    ]

    news = models.ForeignKey(News, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to=news_file_path)
    file_type = models.CharField(max_length=4, choices=FILE_TYPES)

    def __str__(self):
        return f'{self.news.title} - {self.get_file_type_display()}'
