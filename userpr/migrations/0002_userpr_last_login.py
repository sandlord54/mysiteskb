# Generated by Django 2.1.7 on 2019-05-08 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpr',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]