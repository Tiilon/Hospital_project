from django.urls import path
from .views import *

app_name = 'department'

urlpatterns =[
    path('dept_dashboard/', dept_dashboard, name='dashboard'),
    path('patients/', Patients.as_view(), name = 'patients'),
    path('patient/add/', NewPatient.as_view(), name = 'add-patient'),
    path('patient/<id>/', PatientDetails.as_view(), name = 'patient-details'),
]