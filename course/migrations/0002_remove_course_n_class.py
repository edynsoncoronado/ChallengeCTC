# Generated by Django 4.0.1 on 2022-01-15 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='n_class',
        ),
    ]
