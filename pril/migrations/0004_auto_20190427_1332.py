# Generated by Django 2.1.7 on 2019-04-27 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pril', '0003_auto_20190427_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='golos',
            name='timemomenst',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pril.Moment'),
        ),
    ]
