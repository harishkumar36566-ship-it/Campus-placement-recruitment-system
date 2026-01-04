from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('register/', views.register_student, name='register_student'),
    path('students/', views.view_students, name='view_students'),

    path('add-company/', views.add_company, name='add_company'),
    path('companies/', views.view_companies, name='view_companies'),

    path('eligible-companies/<int:student_id>/', views.eligible_companies, name='eligible_companies'),
    path('delete-student/<int:student_id>/', views.delete_student, name='delete_student'),
]