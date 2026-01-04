from django.db import models


# -------------------------
# STUDENT MODEL
# -------------------------
class Student(models.Model):
    name = models.CharField(max_length=100)
    register_no = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=50)

    # CGPA must be NUMBER for eligibility
    cgpa = models.DecimalField(max_digits=3, decimal_places=2)

    photo = models.ImageField(upload_to='students/photos/', blank=True, null=True)
    resume = models.FileField(upload_to='students/resumes/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.register_no})"


# -------------------------
# COMPANY MODEL
# -------------------------
class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    job_role = models.CharField(max_length=100)

    # PACKAGE AS TEXT (allows "6 LPA", "7.5 LPA")
    package = models.CharField(max_length=20)

    # Minimum CGPA for eligibility
    min_cgpa = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name