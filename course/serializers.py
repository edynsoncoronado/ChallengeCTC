from pyexpat import model
from rest_framework import serializers
from .models import CourseClass, Course, Enrollment


class CourseClassSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = CourseClass
        fields = [
            'id', 'code', 'classroom', 'teacher_name', 'horary',
            'frequency', 'center', 'start_day', 'end_day',
            'n_sessions', 'course'
        ]

class CourseSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'id', 'name', 'year', 'month'
        ]


class EnrollmentSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = [
            'id', 'n_invoice', 'currency', 'student', 'partner', 'course', 'state'
        ]
