from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    standard=models.CharField(max_length=50)
    phone_no=models.BigIntegerField()
    username=models.CharField(max_length=50,default='No Name',blank='True')
    password=models.CharField(max_length=50,default='No Name',blank='True')