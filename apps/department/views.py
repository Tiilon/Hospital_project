from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms

# Create your views here.
from apps.management.models import Patient, MedicalDiagnosis, Treatment


@login_required()
def dept_dashboard(request):
    return render(request=request, template_name='department/dept_dashboard.html')

class NewPatient(LoginRequiredMixin, CreateView):
    template_name = 'department/new_patient.html'
    form_class = forms.NewPatientForm
    queryset = Patient.objects.all()
    success_url = reverse_lazy('department:patients')

    def form_valid(self, form):
        valid = super(NewPatient, self).form_valid(form)

        form.instance.created_by = self.request.user
        form.save()

        return valid

class Patients(LoginRequiredMixin, ListView):
    template_name = 'department/patients.html'
    queryset = Patient.objects.all()
    model = Patient

class PatientDetails(LoginRequiredMixin, DetailView):
    template_name = 'department/patient_details.html'
    model = Patient
    queryset = Patient.objects.all()
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super(PatientDetails,self).get_context_data(**kwargs)
        context['age'] = round((timezone.now().date()-self.object.date_of_birth).days/365)
        return context

@login_required()
def vital_sign(request, id):
    patient = Patient.objects.get(id = id)
    weight = request.POST.get('weight')
    sys = request.POST.get('sys')
    dias = request.POST.get('dias')
    respiration = request.POST.get('respiration')
    temperature = request.POST.get('temperature')

    bp = f"{sys}/{dias}"

    patient.weight = weight + 'kg'
    patient.bp = bp + 'mmHg'
    patient.respiration = respiration + 'cpm'
    patient.temperature = temperature + '°C'
    patient.patient_type = 'OPD'

    patient.save()

    return HttpResponseRedirect(reverse_lazy('department:patient-details', kwargs={'id':patient.id}))

class VitalSigns(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('department:patient-details', kwargs={'id': kwargs.get('id')})

    def post(self, request, *args, **kwargs):
        patient = Patient.objects.get(id=kwargs.get('id'))
        weight = request.POST.get('weight')
        sys = request.POST.get('sys')
        dias = request.POST.get('dias')
        respiration = request.POST.get('respiration')
        temperature = request.POST.get('temperature')

        bp = f"{sys}/{dias}"
        if request.method == 'POST':
            patient.weight = weight + 'kg'
            patient.bp = bp + 'mmHg'
            patient.respiration = respiration + 'cpm'
            patient.temperature = temperature + '°C'
            patient.patient_type = 'OPD'

        patient.save()
        return super(VitalSigns, self).post(self,request,*args,**kwargs)

class OPDPatients(LoginRequiredMixin, ListView):
    template_name = 'department/opd.html'
    queryset = Patient.objects.filter(patient_type='OPD')
    model = Patient

class PatientDiagnosis(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('department:patient-details', kwargs={'id':kwargs.get('id')})


    def post(self, request, *args, **kwargs):
        patient = Patient.objects.get(id = kwargs.get('id'))
        complaints = request.POST.get('complaints')
        symptoms = request.POST.get('symptoms')
        diagnosis = request.POST.get('diagnosis')
        is_admitted = request.POST.get('is_admitted')
        onset = request.POST.get('onset')
        treatment = request.POST.get('treatment')

        if is_admitted == 'True':
            admitted = True
        else:
            admitted = False

        md = MedicalDiagnosis.objects.create(
            patient = patient,
            complaints = complaints,
            symptoms= symptoms,
            diagnosis= diagnosis,
            is_admitted= admitted,
            onset= onset,
            created_by= self.request.user
        )

        tmt = Treatment.objects.create(
            diagnosis = md,
            treatment= treatment,
            status= 'Pending',
            created_by=self.request.user

        )

        md.treatments.add(tmt)

        if admitted:
            patient.patient_type = 'Ward'

        patient.diagnoses.add(md)

        md.save()
        patient.save()

        return super(PatientDiagnosis, self).post(self, request, *args, **kwargs)