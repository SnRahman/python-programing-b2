# Generated by Django 5.0 on 2024-01-11 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='prfile_img',
            new_name='profile_img',
        ),
    ]
