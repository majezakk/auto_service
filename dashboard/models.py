from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Vehicle(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    license_plate = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.license_plate})"

class Service(models.Model):
    service_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.service_name

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50, blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"
