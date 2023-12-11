from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import StudentForm,UserReg,UserLogin
from django.contrib.auth import login, authenticate
from .models import Course, Department,Purpose,Material



def load_course(request):
    departmen_id=request.GET.get('departmen_id')
    courses=Course.objects.filter(department_id=departmen_id).all()
    return render(request, 'course.html',{'courses':courses})


def index(request):
    department=Department.objects.all()
    return render(request, "index.html",{'depts': department})

def home(request):
    department=Department.objects.all()
    return render(request, "home.html",{'depts': department})

def user_logout(request):
    auth.logout(request)
    return redirect('/')

def user_login(request):
    department=Department.objects.all()
    if request.method == 'POST':
        form = UserLogin(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('sign:home') 
    else:
        form = UserLogin()
    return render(request, 'login.html', {'form': form,'depts': department})

def register(request):
    department=Department.objects.all()
    if request.method == 'POST':
        form = UserReg(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('sign:login')
    else:
        form = UserReg()
    return render(request, 'reg.html', {'form': form,'depts': department})



def register_student(request):
    department=Department.objects.all()
    purposes=Purpose.objects.all()
    materials=Material.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign:order')
    else:
        form = StudentForm()

    return render(request, 'register_student.html', {'form': form,'department': department, 'purposes': purposes,'materials': materials, 'depts': department})

def order(request):
    department=Department.objects.all()
    return render(request, 'order.html', {'depts': department})