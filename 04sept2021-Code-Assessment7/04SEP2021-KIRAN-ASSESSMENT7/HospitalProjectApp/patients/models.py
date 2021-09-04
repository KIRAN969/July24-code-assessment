from django.db import models

# Create your models here.
class Patient(models.Model):
    p_code=models.IntegerField()
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    mail=models.CharField(max_length=50)
    phone_no=models.BigIntegerField()
    pincode=models.IntegerField()
    username=models.CharField(max_length=50,default='No Name',blank='True')
    password=models.CharField(max_length=50,default='No Name',blank='True')
