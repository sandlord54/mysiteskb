# Generated by Django 2.1.7 on 2019-06-03 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pril', '0020_peoplincollect'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peoplincollect',
            name='nazvsobr',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='nazvsobr', to='pril.Collect'),
        ),
    ]