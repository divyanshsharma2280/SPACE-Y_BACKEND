from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class EmployeeManager(BaseUserManager):
    def create_employee(self, employee_id, password=None, **kwargs):
        if not employee_id:
            raise ValueError('The employee ID must be set')

        employee = self.model(employee_id=employee_id, **kwargs)
        if password:
            employee.set_password(password)
        employee.save(using=self._db)
        return employee

    def create_superuser(self, employee_id, password=None, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_employee(employee_id, password, **kwargs)


class Employee(AbstractBaseUser, PermissionsMixin):
    employee_id = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)  # Storing the hashed password
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=2)
    address = models.CharField(max_length=500)
    designation = models.CharField(max_length=500)
    salary = models.CharField(max_length=10)
    last_login = models.DateTimeField(blank=True, null=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'employee_id'
    REQUIRED_FIELDS = ['name', 'age', 'address', 'designation', 'salary']

    objects = EmployeeManager()

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
