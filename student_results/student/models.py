from django.db import models
from django.contrib.auth.models import User
from Cryptodome.SelfTest.Cipher.test_DES3 import key
import datetime
# Create your models here.
class StudentInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional attributes you want
    student_id = models.CharField(max_length=10, unique=True)
    branch = models.CharField(max_length=27, null=True)
    joining_year = models.IntegerField(null=True)
    section = models.CharField(max_length=5, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.student_id

class StudentSemesterDetail(models.Model):
    YEAR_CHOICES = (
        ('1', "First year"),
        ('2', "Second year"),
        ('3', "Third year"),
        ('4', "Fourth year"),
    )
    student_id = models.ForeignKey(StudentInfo, to_field='student_id', on_delete=models.CASCADE)
    year =  models.CharField(choices=YEAR_CHOICES, max_length=1)
    subj1 = models.IntegerField()
    subj2 = models.IntegerField()
    subj3 = models.IntegerField()

# class CourseList(models.Model):
#     subject_name = CharField

# class StudentCourseDetail(models.Model):
#     subject_name = FK
#     student_id = FK