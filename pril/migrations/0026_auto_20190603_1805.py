# Generated by Django 2.1.7 on 2019-06-03 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pril', '0025_auto_20190603_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collect',
            name='flagin',
        ),
        migrations.AlterField(
            model_name='golos',
            name='flag',
            field=models.BooleanField(default=False, verbose_name='flag'),
        ),
        migrations.DeleteModel(
            name='Flag',
        ),
    ]
