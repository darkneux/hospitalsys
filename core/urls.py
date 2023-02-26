from django.urls import path
from . import views
urlpatterns = [
    path('',views.core,name="home"),
    path('login/',views.loginPage,name='logout'),
    path('patientlist/<patient_id>/',views.patientInfo,),
    path('patientlist/',views.patientList,name='patient_list'),
    path('addpatient/',views.addPatient,name='add_patient'),
]
