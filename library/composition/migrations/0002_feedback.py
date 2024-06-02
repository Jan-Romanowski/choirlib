# Generated by Django 5.0.6 on 2024-06-02 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('composition', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=45, verbose_name='username')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('message', models.TextField(verbose_name='message')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
