# Generated by Django 3.1.4 on 2020-12-19 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stationery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stationery',
            name='Stationery_progress',
        ),
    ]
