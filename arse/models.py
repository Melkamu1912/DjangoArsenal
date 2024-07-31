from django.db import models

# Create your models here.
class product(models.Model):
    Name = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Description = models.TextField()
class Order(models.Model):
    Order_Amount = models.DecimalField(max_digits=10, decimal_places=2)
    Order_Date = models.DateTimeField()

class Customer(models.Model):
    Name = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
class Payment(models.Model):
    Type = models.CharField(max_length=50)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
class Cart(models.Model):
    userId = models.ForeignKey(Customer,on_delete=models.CASCADE)
class Category(models.Model):
    Name = models.CharField(max_length=255)
    picture = models.FileField('upload')
    Description = models.TextField()

