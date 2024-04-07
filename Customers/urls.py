from django.urls import path
from .views import *

urlpatterns = [
    path('api/form/', billing_form_view, name='billing_form'),
    path('api/', BillingAPIView.as_view(), name='billing'),
    path('api/customers/<int:pk>/', CustomerUpdateAPIView.as_view(), name='customer-update'),
    path('api/customers/<int:pk>/delete/', CustomerDeleteAPIView.as_view(), name='customer-delete'),
]