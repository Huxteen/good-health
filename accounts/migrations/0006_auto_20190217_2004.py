# Generated by Django 2.0.7 on 2019-02-17 19:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20190217_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_joined',
        ),
        migrations.AddField(
            model_name='user',
            name='date_join',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='date join'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(auto_now_add=True, verbose_name='last login'),
        ),
    ]
