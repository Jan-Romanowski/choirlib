# Generated by Django 5.0.7 on 2024-07-15 12:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_users_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='date',
            field=models.CharField(default=datetime.datetime(2024, 7, 15, 12, 56, 31, 499736), max_length=20, verbose_name='createDate'),
        ),
    ]
