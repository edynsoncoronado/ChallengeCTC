# Generated by Django 4.0.1 on 2022-01-15 17:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='email',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='partner',
            name='last_name',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='partner',
            name='phone',
            field=models.CharField(default='', max_length=16),
        ),
        migrations.AddField(
            model_name='partner',
            name='second_last_name',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='partner',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 1, 15, 17, 44, 8, 228102, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='partner',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]
