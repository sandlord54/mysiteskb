# Generated by Django 2.1.7 on 2019-05-06 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pril', '0005_auto_20190506_1911'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moment',
            old_name='nazvv',
            new_name='nazv',
        ),
    ]
