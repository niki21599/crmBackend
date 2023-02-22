

from django.db import models
from datetime import date

# Create your models here.

PRODUCT_CATEGORIES = (("digital", "Digital Products"),
("healthcare", "Healthcare"),
("household", "Household"), 
("sport", "Sport"))


REGIONS = (("China", "China"), ("Germany","Germany" ), ("USA", "USA"),("Frankreich", "Frankreich"))


class Customer(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    birthdate = models.DateField(default=date.today)
    email = models.CharField(max_length=500)
    street = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    zip = models.IntegerField()
    region = models.CharField(max_length=20, choices=REGIONS, default="digital")
    
    

class SalesPerson(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    

class Sale(models.Model): 
    created_at = models.DateField(default=date.today)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    salesPerson = models.ForeignKey(SalesPerson, on_delete=models.CASCADE, null=True)
    productCategory = models.CharField(max_length=20, choices=PRODUCT_CATEGORIES, default="digital")
    sales = models.FloatField()