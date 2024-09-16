# Generated by Django 5.0.7 on 2024-09-16 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repertoir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=550, verbose_name='title')),
                ('text', models.CharField(max_length=100, verbose_name='text')),
            ],
            options={
                'verbose_name': 'Repertoir',
                'verbose_name_plural': 'Repertoirs',
            },
        ),
    ]
