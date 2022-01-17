from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .serializers import EnrollmentSerializerDetail
from .models import Enrollment

# Create your tests here.
class GetAllEnrollmentTest(TestCase):

    def test_get_all_enrollments(self):
        response = self.client.get(reverse('enrollments_get'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_enrollmentsactive(self):
        obj_enrollment_active = Enrollment.objects.all().filter(state='active')
        self.assertEqual(obj_enrollment_active.count(), Enrollment.enrollment_active.count())
