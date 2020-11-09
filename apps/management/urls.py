from django.urls import path
from .views import *

app_name = 'management'

urlpatterns =[
    path('dashboard/', dashboard, name='dashboard'),
    path('staff/', staff_list, name= 'staff'),
    path('staff/add/', AddStaff.as_view(), name='staff-add'),
    path('staff/<id>/', StaffDetails.as_view(), name= 'staff-details'),
    path('ward/', ManagerView.as_view(), name = 'wards'),
    path('ward/add/', AddWard.as_view(), name = 'ward-add'),
    path('ward/<id>/', ward_details, name= 'ward-details'),
    path('bill/add/', AddBill.as_view(), name='bill-add'),
    path('bill/del/<bill_id>/', DelBill.as_view(), name='bill-delete'),
    path('bill/update/<bill_id>/', UpdateBill.as_view(), name= 'bill-update'),
    path('hr/', hr_view, name='hr_view'),
    path('hr_resolve/<id>/', resolve_complaint, name='resolve'),
    path('hr/complaint/details/<id>/', complaint_details, name='complaint_details'),
    path('hr/respond/<id>/', response, name = 'response'),
    path('request/add/', MakeRequest.as_view(), name='request-add'),
    path('request/', Requests.as_view(), name= 'requests'),
    path('request/<request_id>/', ChangeRequestStatus.as_view(), name= 'change-request-status')

]