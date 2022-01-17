from django.contrib import admin
from .models import Course, CourseClass, Enrollment

admin.site.register(CourseClass)
admin.site.register(Course)
admin.site.register(Enrollment)
