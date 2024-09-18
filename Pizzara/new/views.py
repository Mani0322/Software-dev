from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth import logout as auth_logout
from . models import Employee,Projects
from django.urls import reverse
import datetime
from datetime import datetime
from .serializers import Employeeserializer,Projectsserializer

from django.contrib import messages

# Create your views here.


def index(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')


def login(request):

    if request.method=="POST":
        username = request.POST.get("username","")
        password = request.POST.get("password","")
        print(username)
        print(password)

        if not username and not password:
            messages.error(request,"Username and Password cannot be empty. please fill them.")
        elif not username and password:
            messages.error(request,"Username cannot be empty.Please fill it.")
        elif username and not password:
            messages.error(request,"Password cannot be empty.Please fill it.")
        else:
            user = authenticate(request,username=username,password=password)
            if user is not None:
                auth_login(request,user)
                return redirect('projects')
            else:
                messages.error(request,"Invalid username and password")
         
        

    return render(request,'login.html')


def signup(request):
    if request.method=="POST":
        first_name = request.POST.get("Firstname","")
        last_name = request.POST.get("Lastname","")
        email = request.POST.get("Email","")
        password = request.POST.get("Password","")
        confirm_password = request.POST.get("Confirm_password","")
        emp = Employee()
        emp.First_name = first_name
        emp.Last_name = last_name
        emp.Email = email
        emp.Password = password
        emp.Confirm_password = confirm_password
        if password == confirm_password:
            emp.save()
            return redirect('login')
        else:
            messages.error(request,"Password mismatched. Please enter the valid password.")



    return render(request,'signup.html')


def projects(request):
    projects = Projects.objects.all()
    # serializer = Projectsserializer(projects)
    # print(serializer.data)
    return render(request,'projects.html',{"projects":projects})

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        messages.success(request,"You have been logged out successfully.")
    return render(request,'logout.html')


def add_projects(request):
    if request.method=='POST':
        project_name = request.POST['project name']
        project_head = request.POST['project head']
        project_startdate = request.POST['project startdate']
        project_enddate = request.POST['project enddate']
        project_members = request.POST['project members']
        status = request.POST['status']
        start_date = datetime.strptime(project_startdate, '%Y-%m-%d').date() if project_startdate else None
        end_date = datetime.strptime(project_enddate, '%Y-%m-%d').date() if project_enddate else None
        members_count = int(project_members) if project_members.isdigit() else 0
        status_value = int(status) if status.isdigit() else 0
        pro = Projects()
        pro.Project_name = project_name
        pro.Project_head = project_head
        pro.Project_startdate = start_date
        pro.Project_enddate = end_date
        pro.project_members = members_count
        pro.status = status_value
        pro.save()
        return redirect('projects')
    return render(request,'add_projects.html')


    
def update(request,id):
    project_update = Projects.objects.get(id=id)
    if request.method=="POST":
        project_name = request.POST['project name']
        project_head = request.POST['project head']
        project_startdate = request.POST['project startdate']
        project_enddate = request.POST['project enddate']
        project_members = request.POST['project members']
        status = request.POST['status']
        start_date = datetime.strptime(project_startdate, '%Y-%m-%d').date() if project_startdate else None
        end_date = datetime.strptime(project_enddate, '%Y-%m-%d').date() if project_enddate else None
        members_count = int(project_members) if project_members.isdigit() else 0
        status_value = int(status) if status.isdigit() else 0
        project_update.Project_name = project_name
        project_update.Project_head = project_head
        project_update.Project_startdate = start_date
        project_update.Project_enddate = end_date
        project_update.project_members = members_count
        project_update.status = status_value
        project_update.save()
        return redirect(reverse('projects'))
    
    return render(request,'update.html',{"data":project_update})

def delete(request,id):
    print(id)
    project_delete = Projects.objects.get(id=id)
    project_delete.delete()
    return redirect(reverse('projects'))