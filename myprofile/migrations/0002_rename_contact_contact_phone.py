# Generated by Django 5.1.5 on 2025-01-31 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='contact',
            new_name='phone',
        ),
    ]
