from django.db import models

# Create your models here.
class Doctor(models.Model):
    d_code=models.IntegerField()
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    specilization=models.CharField(max_length=50)
    phone_no=models.BigIntegerField()
    mail=models.CharField(max_length=50)
    username=models.CharField(max_length=50,default='No Name',blank='True')
    password=models.CharField(max_length=50,default='No Name',blank='True')
