# Generated by Django 5.0.7 on 2024-08-01 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('composition', '0004_remove_composition_changedate'),
    ]

    operations = [
        migrations.AddField(
            model_name='composition',
            name='isActual',
            field=models.BooleanField(default=False, verbose_name='isActual'),
        ),
    ]
