from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def register_user(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    template_name='AccountsApp/register.html'
    context={'form':form}
    return render(request, template_name, context)

def login_view(request):
    if request.method=="POST":
        unm=request.POST.get('un')
        pwd = request.POST.get('pw')
        user=authenticate(username=unm,password=pwd)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'Invalid Credentials')
    template_name='AccountsApp/Login.html'
    context={}
    return render(request, template_name, context)


def logout_view(request):
    logout(request)
    return redirect('login')
