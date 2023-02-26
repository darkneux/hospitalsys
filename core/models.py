from django.db import models
from django_countries.fields import CountryField
# Create your models here.



class Patient_Info(models.Model):
    patient_ID = models.BigAutoField(primary_key=True)
    first_Name = models.CharField(max_length=64,null=False)
    last_Name = models.CharField(max_length=64)
    sex = models.CharField(max_length=10,null=False)
    age = models.IntegerField(null=False)
    nationality = models.CharField(max_length=20,default='Indian')
    address = models.TextField()
    insurance_policy_ID =models.CharField(max_length=12,null=True,blank=True)
    Nation_Card_ID = models.CharField(max_length=15,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    admit_date = models.DateField(auto_now_add=True)
    discharge_date = models.DateField(null=True)
    phone = models.CharField(max_length=15,null=True)