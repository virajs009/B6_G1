from unicodedata import name
from django.db import models

# Create your models here.

class student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)


    class Meta:
        db_table = "student"


 
    