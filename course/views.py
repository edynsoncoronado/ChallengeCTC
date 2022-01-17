from errno import ENOPROTOOPT
from django.http import request
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import CourseClass, Course, Enrollment
from .serializers import CourseClassSerializerDetail, CourseSerializerDetail, EnrollmentSerializerDetail


@api_view(['GET', 'POST'])
def course_list(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializerDetail(courses, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CourseSerializerDetail(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def course_class_list(request):
    if request.method == 'GET':
        courses_class = CourseClass.objects.all()
        serializer = CourseClassSerializerDetail(courses_class, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CourseClassSerializerDetail(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def enrollment_list(request):
    if request.method == 'GET':
        enrollments = Enrollment.objects.all()
        serializer = EnrollmentSerializerDetail(enrollments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EnrollmentSerializerDetail(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def enrollment_detail(request, pk):
    try:
        enrollment = Enrollment.objects.get(pk=pk)
    except Enrollment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EnrollmentSerializerDetail(enrollment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EnrollmentSerializerDetail(enrollment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        enrollment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
