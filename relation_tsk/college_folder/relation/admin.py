from django.contrib import admin
from .models import Student,Lecturer,Department
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','Name','DOB','Email','Dept_name']

admin.site.register(Student,StudentAdmin)


class LecturerAdmin(admin.ModelAdmin):
    list_display = ['id','lect_Name','Email']


admin.site.register(Lecturer, LecturerAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id','Dept_name']


admin.site.register(Department, DepartmentAdmin)