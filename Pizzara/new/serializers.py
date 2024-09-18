from .models import Employee,Projects
from rest_framework import serializers

class Employeeserializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["First_name","Last_name"," Email","Password","Confirm_password"]


class Projectsserializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ["Project_name","Project_head","Project_startdate","Project_enddate","project_members","status"]