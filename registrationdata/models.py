from django.db import models

# Create your models here.
class Registaration(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    age=models.CharField(max_length=3)
    number=models.CharField(max_length=12)
    alt_number=models.CharField(max_length=12)
    email=models.EmailField()
    country=models.CharField(max_length=15)
    password=models.CharField(max_length=20)
    
    class Meta:
        db_table="registration"