from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from apps.management.models import Treatment
from .models import *

# Create your views here.
from django.views.generic import ListView, DetailView


def dashboard(request):
    return render(request, 'pharmacy/dashboard.html' )

class Medicines(ListView, LoginRequiredMixin):
    model = Medicine
    queryset = Medicine.objects.all()
    template_name = 'pharmacy/medicines.html'


class Treatments(LoginRequiredMixin, ListView):
    model = Treatment
    queryset = Treatment.objects.exclude(prescription=None)
    template_name = 'pharmacy/treatments.html'


class TreatmentDetails(LoginRequiredMixin, DetailView):
    model = Treatment
    queryset = Treatment.objects.exclude(prescription=None)
    template_name = 'pharmacy/treatment_details.html'
    pk_url_kwarg = 'id'

class MedicineDetails(LoginRequiredMixin, DetailView):
    model = Medicine
    queryset = Medicine.objects.all()
    template_name = 'pharmacy/medicine_detail.html'
    pk_url_kwarg = 'id'