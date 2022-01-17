# Generated by Django 4.0.1 on 2022-01-16 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_enrollment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='state',
            field=models.CharField(choices=[('draft', 'Borrador'), ('active', 'Activo'), ('done', 'Terminado'), ('cancel', 'Cancelado')], default='draft', max_length=16),
        ),
    ]
