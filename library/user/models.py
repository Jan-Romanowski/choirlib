from django.db import models


class User(models.Model):
    name = models.CharField('name', max_length=25)
    surname = models.CharField('surname', max_length=25)
    email = models.CharField('email', max_length=30)
    password = models.CharField('password', max_length=51)
    date = models.DateTimeField('regDate')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    