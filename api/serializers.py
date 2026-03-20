from rest_framework import serializers
from students.models import Student
from employees.models import Employee

class StudentSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class EmployeeSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"








