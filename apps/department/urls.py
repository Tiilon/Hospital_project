from django.urls import path
from .views import *

app_name = 'department'

urlpatterns =[
    path('dept_dashboard/', dept_dashboard, name='dashboard'),
]