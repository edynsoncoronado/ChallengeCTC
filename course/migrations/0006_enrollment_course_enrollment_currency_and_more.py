# Generated by Django 4.0.1 on 2022-01-16 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0009_alter_country_code'),
        ('course', '0005_remove_enrollment_course_remove_enrollment_currency_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.course'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='currency',
            field=models.CharField(choices=[('USD', 'Dolar'), ('PEN', 'Soles')], default='PEN', max_length=3),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='partner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='enrollment_ids', to='partner.partner'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='state',
            field=models.CharField(choices=[('draft', 'Borrador'), ('active', 'Activo'), ('done', 'Terminado'), ('cancel', 'Cancelado')], default='draft', max_length=16),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='enrollment_ids', to='partner.student'),
        ),
    ]
