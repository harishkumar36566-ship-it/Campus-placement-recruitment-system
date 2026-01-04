from django import forms
from .models import Student, Company

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'location', 'job_role', 'package', 'min_cgpa']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'job_role': forms.TextInput(attrs={'class': 'form-control'}),
            'package': forms.TextInput(attrs={'class': 'form-control'}),
            'min_cgpa': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': 'Eg: 6.5'
            }),
        }