# Generated by Django 2.1.7 on 2019-05-30 11:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userpr', '0002_userpr_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpr',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='userpr',
            name='password',
        ),
        migrations.RemoveField(
            model_name='userpr',
            name='username',
        ),
        migrations.AddField(
            model_name='userpr',
            name='full_name',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='userpr',
            name='user',
            field=models.OneToOneField(default=4, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userpr',
            name='email',
            field=models.CharField(default=None, max_length=500),
        ),
    ]