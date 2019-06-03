# Generated by Django 2.1.7 on 2019-06-03 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pril', '0023_auto_20190603_1343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collect',
            name='flagin',
        ),
        migrations.RemoveField(
            model_name='golos',
            name='timemomenst',
        ),
        migrations.AddField(
            model_name='golos',
            name='namesobr',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='namesobr', to='pril.Collect'),
        ),
    ]
