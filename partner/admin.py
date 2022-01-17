from django.contrib import admin
from django import forms
from .models import Partner, Student, Country, DocumentType


admin.site.register(Partner)
admin.site.register(Student)
admin.site.register(Country)
admin.site.register(DocumentType)
