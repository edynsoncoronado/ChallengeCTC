from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.course_list),
    path('classes/', views.course_class_list),
    path('enrollments/', views.enrollment_list, name='enrollments_get'),
    path('enrollments/<int:pk>', views.enrollment_detail),
]
