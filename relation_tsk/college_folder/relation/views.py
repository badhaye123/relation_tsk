from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Student, Lecturer, Department
from .forms import StudentForm, LecturerForm, DepartmentForm
from django.http import HttpResponse


# Create your views here.
@login_required(login_url='login')
def stu_add(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showstud')
    template_name = 'relation/studentadd.html'
    context = {'form': form}
    return render(request, template_name, context)

@login_required(login_url='login')
def dept_add(request):
    records = Department.objects.all()
    print(records)
    flag = 'Not Available'
    form = DepartmentForm()
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            for i in records:
                if i.Dept_name == form.cleaned_data['Dept_name']:
                    flag = 'Record already exist'
                    return HttpResponse(f'{flag}')
            form.save()
            return redirect('showdept')
    template_name = 'relation/deptadd.html'
    context = {'form': form}
    return render(request, template_name, context)

@login_required(login_url='login')
def lect_add(request):
    form = LecturerForm()
    if request.method == "POST":
        form = LecturerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showlect')
    template_name = 'relation/lectadd.html'
    context = {'form': form}
    return render(request, template_name, context)

@login_required(login_url='login')
def stu_delete(request, id):
    record = Student.objects.get(id=id)
    record.delete()
    return redirect('showstud')

@login_required(login_url='login')
def lect_delete(request, id):
    record = Lecturer.objects.get(id=id)
    print(len(record.Dept_name.all()))
    record.delete()
    return redirect('showlect')

@login_required(login_url='login')
def dept_delete(request, id):
    record = Department.objects.get(id=id)
    data = Lecturer.objects.filter(Dept_name=record)
    for i in data:
        for j in i.Dept_name.all():
            if len(i.Dept_name.all()) == 1 and j == record:
                i.delete()
    record.delete()
    return redirect('showdept')

@login_required(login_url='login')
def stu_update(request, id):
    record = Student.objects.get(id=id)
    form = StudentForm(instance=record)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('showstud')
    template_name = 'relation/studentadd.html'
    context = {'form': form}
    return render(request, template_name, context)

@login_required(login_url='login')
def lect_update(request, id):
    record = Lecturer.objects.get(id=id)
    form = LecturerForm(instance=record)
    if request.method == 'POST':
        form = LecturerForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('showlect')
    template_name = 'relation/lectadd.html'
    context = {'form': form}
    return render(request, template_name, context)

@login_required(login_url='login')
def dept_update(request, id):
    record = Department.objects.get(id=id)
    form = DepartmentForm(instance=record)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('showdept')
    template_name = 'relation/deptadd.html'
    context = {'form': form}
    return render(request, template_name, context)

@login_required(login_url='login')
def show_stud(request):
    records = Student.objects.all()
    template_name = 'relation/showstudent.html'
    context = {'records': records}
    return render(request, template_name, context)

@login_required(login_url='login')
def show_lect(request):
    records = Lecturer.objects.all()
    template_name = 'relation/showlect.html'
    context = {'records': records}
    return render(request, template_name, context)

@login_required(login_url='login')
def show_dept(request):
    records = Department.objects.all()
    template_name = 'relation/showdept.html'
    context = {'records': records}
    return render(request, template_name, context)


def home(request):
    template_name = 'relation/home.html'
    context = {}
    return render(request, template_name, context)

@login_required(login_url='login')
def search(request):
    print('get form')
    if request.method == 'POST':
        srch = request.POST.get('searchkey')
        print(srch)
        record = Student.objects.filter(Name__icontains=srch)
        print(record)
        recordlect = Lecturer.objects.filter(lect_Name__icontains=srch)
        print(recordlect)
        print(len(record), "recordlength", len(recordlect), "recordlength")
        context = {'record': record, 'recordlect': recordlect}
        return render(request, 'relation/showresult.html', context)
    template_name = 'relation/search.html'
    context = {}
    return render(request, template_name, context)

@login_required(login_url='login')
def search_dept_stu(request, id):
    data = Department.objects.get(id=id)
    record = Student.objects.filter(Dept_name=data)
    print(record)
    template_name = 'relation/showdeptstudent.html'
    context = {'record': record}
    return render(request, template_name, context)

@login_required(login_url='login')
def search_dept_lect(request, id):
    data = Department.objects.get(id=id)
    record = Lecturer.objects.filter(Dept_name=data)
    print(record)
    template_name = 'relation/showdeptlect.html'
    context = {'record': record}
    return render(request, template_name, context)