# Generated by Django 4.0.1 on 2022-01-15 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=16)),
            ],
        ),
    ]
