# Generated by Django 5.1.4 on 2024-12-25 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('like', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='saveitem',
            old_name='save',
            new_name='saved',
        ),
    ]
