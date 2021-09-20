from django import forms
from .models import Department,Student,Lecturer


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'



class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'


class LecturerForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = '__all__'

        widgets={
            'Dept_name':forms.CheckboxSelectMultiple()
        }
