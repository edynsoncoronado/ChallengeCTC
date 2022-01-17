from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Partner, Student
from .serializers import StudentSerializer, PartnerSerializer


@api_view(['GET'])
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializers = StudentSerializer(students, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def partner_list(request):
    if request.method == 'GET':
        partners = Partner.objects.all()
        serializers = PartnerSerializer(partners, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
