from django.db import models
from Products.models import Product
from django.db.models import JSONField
from decimal import Decimal


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    items_bought = JSONField(default=dict)
    total_bill = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name

    def calculate_total_bill(self):
        total = Decimal(0)
        for item, units in self.items_bought.items():
            product = Product.objects.get(name=item)
            total += product.price * units
        self.total_bill = total
        self.save()


class BillingList(models.Model):
    items = models.ManyToManyField(Product, related_name='billing_lists')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f'Billing List #{self.id}'

