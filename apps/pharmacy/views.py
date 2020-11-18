from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from apps.management.models import Treatment, Patient
from apps.portal.models import Bill
from .models import *
from django.views.generic import ListView, DetailView, RedirectView
# Create your views here.


def dashboard(request):
    return render(request, 'pharmacy/dashboard.html')


class Medicines(ListView, LoginRequiredMixin):
    model = Medicine
    queryset = Medicine.objects.all()
    template_name = 'pharmacy/medicines.html'


class Treatments(LoginRequiredMixin, ListView):
    model = Treatment
    queryset = Treatment.objects.exclude(prescription=None)
    template_name = 'pharmacy/treatments.html'


# class TreatmentDetails(LoginRequiredMixin, DetailView):
#     model = Treatment
#     queryset = Treatment.objects.exclude(prescription=None)
#     template_name = 'pharmacy/treatment_details.html'
#     pk_url_kwarg = 'id'
#
#     def get_context_data(self, **kwargs):
#         context = super(TreatmentDetails, self).get_context_data(**kwargs)
#
#         try:
#             context['prescription'] = Prescription.objects.get(treatment_id=self.object.id, patient_id=self.object.diagnosis.patient.id)
#         except Prescription.DoesNotExist:
#             pass
#         context['medicines'] = Medicine.objects.exclude(units_left=0)
#         return context
#same as the one above
@login_required
def treatment_details(request, id):
    treatment = Treatment.objects.get(id=id)
    prescription = None
    try:
        prescription = Prescription.objects.get(treatment_id=treatment.id, patient_id=treatment.diagnosis.patient.id)
    except Prescription.DoesNotExist:
        pass

    medicines = None
    total=0
    try:
       medicines = Medicine.objects.exclude(units_left=0)
       for pm in prescription.medicines.all():
           total += pm.amount
    except:
       pass

    context = {
        'object':treatment,
        'prescription':prescription,
        'medicines':medicines,
        'error':'',
        'total':total
    }

    if request.method == 'POST':
        medicine_id = request.POST.get('medicine')
        quantity = request.POST.get('quantity')
        dosage = request.POST.get('dosage')

        medicine = Medicine.objects.get(id=medicine_id)
        amount_total = int(quantity) * medicine.selling_price_per_unit


        try:
            PrescribedMedicine.objects.get(medicine=medicine_id, prescription=prescription)
            context['error'] = 'You have already added this medicine'
            return render(request,'pharmacy/treatment_details.html', context)
        except PrescribedMedicine.DoesNotExist:
            pass

        pm = PrescribedMedicine.objects.create(
            medicine=medicine,
            prescription=prescription,
            quantity = quantity,
            dosage=dosage,
            amount=amount_total,
            created_by=request.user
        )

        prescription.medicines.add(pm)
        prescription.save()
        return redirect(reverse_lazy('pharmacy:treatment-details', kwargs={'id':id}))

    return render(request, 'pharmacy/treatment_details.html', context)


class MedicineDetails(LoginRequiredMixin, DetailView):
    model = Medicine
    queryset = Medicine.objects.all()
    template_name = 'pharmacy/medicine_detail.html'
    pk_url_kwarg = 'id'


class OpenPrescription(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('pharmacy:treatment-details', kwargs={'id': kwargs.get('treatment_id')})

    def get(self, request, *args, **kwargs):
        treatment_id = kwargs.get('treatment_id')
        patient_id = kwargs.get('patient_id')

        treatment = Treatment.objects.get(id = treatment_id)
        patient = Patient.objects.get(id = patient_id)

        new_prescription = Prescription.objects.create(
            patient=patient,
            treatment=treatment,
            status=0,
            created_by=self.request.user
        )

        treatment.pharmacy_prescription = new_prescription
        treatment.save()

        return super(OpenPrescription, self).get(self, *args, **kwargs)


class RemovePrescribedMedicine(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('pharmacy:treatment-details', kwargs={'id': kwargs.get('treatment_id')})

    def get(self, request, *args, **kwargs):
        pm_id = kwargs.get('pm_id')
        pres_id = kwargs.get('pres_id')

        prescription = Prescription.objects.get(id = pres_id)
        prescribed_medicine = PrescribedMedicine.objects.get(id=pm_id, prescription=prescription)

        prescribed_medicine.delete()

        return super(RemovePrescribedMedicine,self).get(self,request,*args,**kwargs)


class ConfirmPrescription(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('pharmacy:treatment-details', kwargs={'id':kwargs.get('treatment_id')})

    def get(self, request, *args, **kwargs):
        prescription = Prescription.objects.get(id = kwargs.get('pres_id'))
        treatment = Treatment.objects.get(id = kwargs.get('treatment_id'))

        total = 0
        for pm in prescription.medicines.all():
            total += pm.amount

        bill = Bill.objects.create(
            bill_type= 'PhB',
            patient=treatment.diagnosis.patient,
            amount=total,
            status=0,
            prescription=prescription,
            created_by=self.request.user
        )

        prescription.total = total
        prescription.status = 1

        prescription.save()

        return super(ConfirmPrescription, self).get(self, request,*args, **kwargs)