# Generated by Django 5.1.1 on 2024-10-05 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repertoir', '0002_alter_repertoir_text_alter_repertoir_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repertoir',
            name='text',
            field=models.CharField(max_length=400, verbose_name='text'),
        ),
        migrations.AlterField(
            model_name='repertoir',
            name='title',
            field=models.CharField(max_length=1500, verbose_name='title'),
        ),
    ]
