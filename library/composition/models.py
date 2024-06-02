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


class Feedback(models.Model):
    username = models.CharField('username', max_length=45)
    email = models.EmailField('email')
    message = models.TextField('message')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'