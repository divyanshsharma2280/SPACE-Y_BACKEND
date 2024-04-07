# urls.py

from django.urls import path
from .views import ProductCreateAPIView, ProductRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/', ProductCreateAPIView.as_view(), name='product-create'),
    path('api/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
]
