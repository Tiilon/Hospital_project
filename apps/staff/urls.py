from django.urls import path
from .views import *

app_name = 'staff'

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('create/', create_complaints, name='create'),
    path('cancel/<id>/', cancel_complaint, name='cancel'),
]