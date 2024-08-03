# Generated by Django 5.0.7 on 2024-08-03 06:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('composition', '0010_alter_composition_folder'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompositionFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='compositions/%Y/%m/%d/')),
                ('file_type', models.CharField(choices=[('mp3', 'MP3 File'), ('wav', 'WAV File'), ('pdf', 'PDF File')], max_length=3)),
                ('composition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='composition.composition')),
            ],
        ),
    ]
