# Generated by Django 2.1.7 on 2019-05-30 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pril', '0017_auto_20190530_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='golos',
            name='username',
        ),
        migrations.AddField(
            model_name='collect',
            name='flagin',
            field=models.ForeignKey(default=32, on_delete=django.db.models.deletion.CASCADE, related_name='flagin', to='pril.Golos'),
            preserve_default=False,
        ),
    ]
