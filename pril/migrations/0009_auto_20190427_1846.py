# Generated by Django 2.1.7 on 2019-04-27 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pril', '0008_collect_lelpeep'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collect',
            name='lelpeep',
        ),
        migrations.AddField(
            model_name='collect',
            name='peopleincoll',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, related_name='peopleincoll', to='pril.Golos'),
            preserve_default=False,
        ),
    ]