from django.db import models

# Create your models here.
class Librarian(models.Model):
    enroll_code=models.IntegerField()
    name=models.CharField(max_length=40)
    address=models.CharField(max_length=40)
    mobile_no=models.BigIntegerField()
    username=models.CharField(max_length=40)
    password=models.IntegerField()