from rest_framework import generics
from .models import Employee
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status


class EmployeeCreateAPIView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeLoginAPIView(generics.GenericAPIView):
    serializer_class = EmployeeLoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        employee_id = serializer.validated_data.get('employee_id')
        password = serializer.validated_data.get('password')

        employee = Employee.objects.filter(employee_id=employee_id).first()

        if not employee:
            return Response({'error': 'Invalid employee ID'}, status=status.HTTP_401_UNAUTHORIZED)

        user = authenticate(request, username=employee.employee_id, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh)
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)