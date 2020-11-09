from django.urls import path
from .views import *

app_name = 'department'

urlpatterns =[
    path('dept_dashboard/', dept_dashboard, name='dashboard'),
    path('patients/', Patients.as_view(), name = 'patients'),
    path('patient/add/', NewPatient.as_view(), name = 'add-patient'),
    path('patient/<id>/', PatientDetails.as_view(), name = 'patient-details'),
    path('patient/vital-signs/<id>/', vital_sign, name = 'vital-signs'),
    path('opd/', OPDPatients.as_view(), name = 'opd'),
    path('patient/diagnosis/add/<id>/', PatientDiagnosis.as_view(), name = 'add-diagnosis'),
    path('patient/note/add/<id>/', pat_notes, name='add-note'),
    path('patient/treatment/add/<patient_id><diagnosis_id>/', add_treatment, name= 'add_treatment'),
    path('patient/treatment/complete/<treatment_id><patient_id>/',complete_treatment, name='complete-treatment'),
    path('patient/treatment/cancel/<treatment_id>/<patient_id>/', CancelTreatment.as_view(), name= 'cancel-treatment'),
    path('wards/', Wards.as_view(), name='wards'),
    path('ward/<id>', ward_details, name='ward-details'),
    path('ward/bed/allocate/<bed_id>/', allocate_bed, name='bed-allocate'),
    path('patient/discharge/<id>/', DischargePatient.as_view(), name ='patient-discharge')
]