# Generated by Django 5.0.7 on 2024-08-02 11:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('composition', '0009_alter_composition_folder'),
        ('folder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='composition',
            name='folder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='compositions', to='folder.folder'),
        ),
    ]
