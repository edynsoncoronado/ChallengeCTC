from errno import ENOPROTOOPT
from random import choice
from django.db import models
from partner.models import Partner, Student


class Course(models.Model):
    name = models.CharField(
        max_length=16
    )
    year = models.IntegerField()
    month = models.CharField(
        max_length=8
    )

    def __str__(self):
        return self.name


class CourseClass(models.Model):
    code = models.CharField(
        max_length=4
    )
    classroom = models.CharField(
        max_length=64
    )
    teacher_name = models.CharField(
        max_length=128
    )
    horary = models.CharField(
        max_length=2,
        choices=[
            ('a', '9:00 - 11:00'),
            ('b', '11:00 - 13:00'),
            ('c', '15:00 - 17:00'),
            ('d', '17:00 - 19:00'),
        ],
        default='a'
    )
    frequency = models.CharField(
        max_length=3,
        choices=[
            ('od', 'Online Dialy'),
            ('lmv', 'L-M-V'),
            ('mj', 'M-J'),
            ('os', 'only S'),
            ('od', 'only D')
        ],
        default='od'
    )
    center = models.CharField(
        max_length=16,
        choices=[
            ('online', 'Online'),
        ],
        default='online'
    )
    start_day = models.DateField()
    end_day = models.DateField()
    n_sessions = models.IntegerField()
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class EnrollmentManager(models.Manager):

    def get_queryset(self):
        return super(EnrollmentManager, self).get_queryset().filter(
            state='active'
        )


class Enrollment(models.Model):
    n_invoice = models.CharField(
        max_length=16,
        default=''
    )
    currency = models.CharField(
        max_length=3,
        choices=[
            ('USD', 'Dolar'),
            ('PEN', 'Soles')
        ],
        default='PEN'
    )
    student = models.ForeignKey(
        Student,
        related_name='enrollment_ids',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    partner = models.ForeignKey(
        Partner,
        related_name='enrollment_ids',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    state = models.CharField(
        max_length=16,
        choices=[
            ('draft', 'Borrador'),
            ('active', 'Activo'),
            ('done', 'Terminado'),
            ('cancel', 'Cancelado')
        ],
        default='draft'
    )
    objects = models.Manager()
    enrollment_active = EnrollmentManager()

    def __str__(self):
        return '{} {}'.format(
            self.n_invoice,
            self.state
        )
