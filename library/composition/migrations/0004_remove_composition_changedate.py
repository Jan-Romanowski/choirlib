# Generated by Django 5.0.7 on 2024-07-26 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('composition', '0003_composition_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='composition',
            name='changeDate',
        ),
    ]
