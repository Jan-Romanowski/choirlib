# Generated by Django 5.1.1 on 2024-10-05 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repertoir', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repertoir',
            name='text',
            field=models.CharField(max_length=200, verbose_name='text'),
        ),
        migrations.AlterField(
            model_name='repertoir',
            name='title',
            field=models.CharField(max_length=1000, verbose_name='title'),
        ),
    ]