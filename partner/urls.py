from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list),
    path('partners/', views.partner_list, name='partner_list')
]
