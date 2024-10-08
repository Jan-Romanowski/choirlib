# Generated by Django 5.0.7 on 2024-08-28 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_user_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('can_view_library', 'Może przeglądać bibliotekę'), ('can_edit_compositions', 'Może edytować utwory'), ('can_edit_folders', 'Może edytować teczki'), ('can_edit_news', 'Może edytować aktualności')]},
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_regular_user',
        ),
    ]
