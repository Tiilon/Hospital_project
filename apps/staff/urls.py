from django.urls import path
from .views import *

app_name = 'staff'

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('create/', create_complaints, name='create'),
    path('cancel/<id>/', cancel_complaint, name='cancel'),
    path('new/leave/', NewStaffLeave.as_view(), name='leave-new'),
    path('staff/leave/list/', staff_leave_list, name='staff-leave-list'),
]