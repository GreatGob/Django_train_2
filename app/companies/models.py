from django.db import models
from django.contrib import admin
from django.utils import timezone
import datetime

# Create your models here.
class Company(models.Model):
    c_name= models.CharField(max_length= 200)
    pub_date= models.DateTimeField('date_published')
    def __str__(self):
        return f"name: {self.c_name}"
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='published recently'
    )
    def was_published_recently(self):
        now=timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <=now
    
class Employee(models.Model):
    company= models.ForeignKey(Company, related_name= 'employee', on_delete=models.CASCADE)
    e_name= models.CharField(max_length=200)
    pub_date= models.DateTimeField('date_published')
    def __str__(self):
        return f"name: {self.e_name}"
    def was_published_recently(self):
        now=timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <=now
    
class More(models.Model):
    employee= models.ForeignKey(Employee, related_name= 'more', on_delete=models.CASCADE)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    age=models.IntegerField()
    pub_date= models.DateTimeField('date_published')
    def __str__(self):
        return f"first name: {self.first_name} | last name:{self.last_name} | age: {self.age}"
    def was_published_recently(self):
        now=timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <=now