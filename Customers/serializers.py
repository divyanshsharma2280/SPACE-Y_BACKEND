# serializers.py

from rest_framework import serializers

from Products.models import Product
from .models import BillingList
from Customers.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'address']


class BillingItemSerializer(serializers.Serializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    quantity = serializers.IntegerField(min_value=1)


class BillingListSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    items = BillingItemSerializer(many=True)

    class Meta:
        model = BillingList
        fields = ['customer', 'items']

    def create(self, validated_data):
        customer_data = validated_data.pop('customer')
        items_data = validated_data.pop('items')

        customer = Customer.objects.create(**customer_data)
        billing_list = BillingList.objects.create(customer=customer)

        total_amount = 0
        for item_data in items_data:
            product = item_data['product_id']
            quantity = item_data['quantity']
            total_amount += product.price * quantity
            billing_list.items.add(product)

        billing_list.total_amount = total_amount
        billing_list.save()

        return billing_list
