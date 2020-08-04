from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=21, null=True)
    student_id = models.CharField(max_length=10, null=True)
    email = models.EmailField(max_length=254, unique=True, null=True)
    branch = models.CharField(max_length=27, null=True)
    current_year = models.IntegerField(null=True)
    section = models.CharField(max_length=5, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

class Student_login(models.Model):
    student_id = models.CharField(max_length=10)
    password = models.CharField(max_length=10)