# Generated by Django 4.0.1 on 2022-01-15 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('n_class', models.IntegerField()),
                ('year', models.IntegerField()),
                ('month', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='CourseClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=4)),
                ('classroom', models.CharField(max_length=64)),
                ('teacher_name', models.CharField(max_length=128)),
                ('horary', models.CharField(choices=[('a', '9:00 - 11:00'), ('b', '11:00 - 13:00'), ('c', '15:00 - 17:00'), ('d', '17:00 - 19:00')], default='a', max_length=2)),
                ('frequency', models.CharField(choices=[('od', 'Online Dialy'), ('lmv', 'L-M-V'), ('mj', 'M-J'), ('os', 'only S'), ('od', 'only D')], default='od', max_length=3)),
                ('center', models.CharField(choices=[('online', 'Online')], default='online', max_length=16)),
                ('start_day', models.DateField()),
                ('end_day', models.DateField()),
                ('n_sessions', models.IntegerField()),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.course')),
            ],
        ),
    ]
