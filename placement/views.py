from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Company
from .forms import StudentForm, CompanyForm


def home(request):
    return render(request, 'placement/home.html')


def dashboard(request):
    students_count = Student.objects.count()
    companies_count = Company.objects.count()
    return render(request, 'placement/dashboard.html', {
        'students_count': students_count,
        'companies_count': companies_count
    })


def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_students')
    else:
        form = StudentForm()
    return render(request, 'placement/register.html', {'form': form})


def view_students(request):
    students = Student.objects.all()
    return render(request, 'placement/view_students.html', {'students': students})


def add_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_companies')
    else:
        form = CompanyForm()
    return render(request, 'placement/add_company.html', {'form': form})


def view_companies(request):
    companies = Company.objects.all()
    return render(request, 'placement/view_companies.html', {'companies': companies})


def eligible_companies(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    companies = Company.objects.filter(min_cgpa__lte=student.cgpa)
    return render(request, 'placement/eligible_companies.html', {
        'student': student,
        'companies': companies
    })
def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('view_students')