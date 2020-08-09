from django import forms
from django.contrib.auth.models import User
from student.models import StudentInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

class StudentInfoForm(forms.ModelForm):
    class Meta():
        model = StudentInfo
        fields = ('student_id','profile_pic','branch','current_year','section')