from django.db import models
from django.contrib import admin
# Create your models here.



class Employee(models.Model):
    employee_id = models.CharField(max_length=100)
    employee_first = models.CharField(max_length=100,)
    employee_last = models.CharField(max_length=100)
    employee_shift = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,null=True,blank=True)
    phone=models.CharField(max_length=100,null=True, blank=True)
    senority=models.IntegerField(null=True,blank=True)
    status=models.CharField(max_length=100,null=True, blank=True)


    def __str__(self):
         return self.employee_first
