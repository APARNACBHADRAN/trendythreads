# Generated by Django 4.2.2 on 2023-07-03 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='Desc',
            new_name='desc',
        ),
    ]
