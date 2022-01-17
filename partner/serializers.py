from rest_framework import serializers
from .models import Partner, Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id', 'code', 'name', 'last_name', 'second_last_name', 'phone',
            'email', 'timestamp', 'document_number', 'country', 'partners'
        ]


class StudentSerializerDetail(serializers.ModelSerializer):

    student_name = serializers.SerializerMethodField('get_student_name')

    def get_student_name(self, obj):
        return '{} {} {}'.format(
            obj.name,
            obj.last_name,
            obj.second_last_name
        )

    class Meta:
        model = Student
        fields = ['id', 'student_name', 'phone', 'email']


class PartnerSerializer(serializers.ModelSerializer):
    students = StudentSerializerDetail(many=True, required=False)

    class Meta:
        model = Partner
        fields = ['id', 'name', 'students']
