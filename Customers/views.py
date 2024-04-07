from rest_framework.response import Response
from rest_framework import generics
from .models import BillingList
from .serializers import BillingListSerializer
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from templates import *
from Products.models import Product
from django.shortcuts import render


def billing_form_view(request):
    return render(request, 'billing_form.html')


class BillingAPIView(generics.CreateAPIView):
    serializer_class = CustomerSerializer

    def create(self, request, *args, **kwargs):
        # Retrieve items and quantities from request data
        items = request.data.get('items', {})
        quantities = request.data.get('quantities', {})

        # Calculate total bill based on items and quantities
        total_bill = 0
        for item, quantity in zip(items, quantities):
            product = Product.objects.get(name=item)
            total_bill += product.price * quantity

        # Add total bill to request data
        request.data['total_bill'] = total_bill

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CustomerUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
