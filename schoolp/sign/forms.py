# forms.py
from django import forms
from django.forms.widgets import DateInput
from .models import StudentForm, Course,Material
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class UserReg(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class UserLogin(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        
    class DateInput(forms.DateInput):
        input_type='date'

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentForm
        dob=date = forms.DateField()

        fields = ['name', 'dob', 'age', 'gender', 'phone_number', 'mail_id', 'address', 'department', 'course', 'purpose', 'materials_provided']

          

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()

        if 'department' in self.data:
            try:
                department = self.data.get('department')
                self.fields['course'].queryset = Course.objects.filter(department_id=department).all()
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set.order_by('name')
