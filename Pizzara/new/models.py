from django.db import models

# Create your models here.


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    First_name = models.CharField(max_length=20,default="")
    Last_name = models.CharField(max_length=20,default="")
    Email = models.EmailField(default="")
    Password = models.CharField(max_length=12,default="")
    Confirm_password = models.CharField(max_length=12,default="")

class Projects(models.Model):
    id = models.AutoField(primary_key=True)
    Project_name = models.CharField(max_length=20,default="")
    Project_head = models.CharField(max_length=20,default="")
    Project_startdate = models.DateField(null=True,blank=True)
    Project_enddate = models.DateField(null=True,blank=True)
    project_members = models.IntegerField(default=0)
    status = models.IntegerField(default=0)

