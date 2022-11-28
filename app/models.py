from django.db import models
from django.contrib import admin
from django.contrib.postgres.fields import ArrayField



class Event(models.Model):
    day = models.DateField(u'Day of the event', help_text=u'Day of the event')
    start_time = models.TimeField(u'Starting time', help_text=u'Starting time')
    end_time = models.TimeField(u'Final time', help_text=u'Final time')
    notes = models.TextField(u'Textual Notes', help_text=u'Textual Notes', blank=True, null=True)

    class Meta:
        verbose_name = u'Scheduling'
        verbose_name_plural = u'Scheduling'

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
