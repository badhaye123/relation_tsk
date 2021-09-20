from django.db import models
# Create your models here.
class Department(models.Model):
    Dept_name = models.CharField(max_length=32)

    def __str__(self):
        return self.Dept_name

class Student(models.Model):
    Name = models.CharField(max_length=64)
    Email = models.EmailField(max_length=64)
    DOB = models.DateField()
    Dept_name = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Name},{self.Email},{self.DOB},{self.Dept_name}'

class Lecturer(models.Model):
    lect_Name = models.CharField(max_length=64)
    Email = models.EmailField(max_length=64)
    Dept_name = models.ManyToManyField(Department)

    def __str__(self):
        return f'{self.lect_Name},{self.Dept_name}'