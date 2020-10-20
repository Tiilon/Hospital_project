from django.urls import path
from.views import *

app_name = 'portal'

urlpatterns = [
    path('portal/', portal_layout, name= 'portal_layout'),
    path('portal_dashboard/', dashboard, name = 'portal_dashboard')
]