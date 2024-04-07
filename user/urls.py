from django.urls import path
from .views import *


urlpatterns = [
    path('api/employees/', EmployeeCreateAPIView.as_view(), name='employee-create'),
path('api/login/', EmployeeLoginAPIView.as_view(), name='employee-login'),
]