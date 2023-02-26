from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Patient_Info

class PatientAdmin(admin.ModelAdmin):
    list_display = ('patient_ID', 'first_Name', 'last_Name', 'sex', 'age', 'nationality', 'insurance_policy_ID','phone', 'email', 'address')

admin.site.register(Patient_Info, PatientAdmin)