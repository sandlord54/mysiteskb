# Generated by Django 2.1.7 on 2019-05-27 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pril', '0014_auto_20190507_1404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collect',
            name='peopleincoll',
        ),
    ]
