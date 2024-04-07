from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name','password', 'employee_id', 'age', 'address', 'designation', 'salary']

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)


class EmployeeLoginSerializer(serializers.Serializer):
    employee_id = serializers.CharField()
    password = serializers.CharField()