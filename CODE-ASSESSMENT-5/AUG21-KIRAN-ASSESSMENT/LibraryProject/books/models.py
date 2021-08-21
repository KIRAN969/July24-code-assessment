from django.db import models

# Create your models here.
class Book(models.Model):
    bookname=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    publisher=models.CharField(max_length=50)
    price=models.IntegerField()