from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class StudentInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional attributes you want
    student_id = models.CharField(max_length=10)
    branch = models.CharField(max_length=27, null=True)
    current_year = models.IntegerField(null=True)
    section = models.CharField(max_length=5, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username
