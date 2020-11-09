from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, RedirectView, TemplateView
from apps.management.forms import UserForm
from apps.pharmacy.models import Medicine
from apps.portal.models import DefaultBills
from apps.staff.forms import ComplaintForm
from apps.user.models import User
from .models import *
from apps.management import models


@login_required()
def dashboard(request):
    return render(request=request, template_name='management/dashboard.html')

@login_required()
def staff_list(request):
    staff = User.objects.all()

    context = {
        'object_list': staff
    }

    return render(request=request, template_name='management/staff_list.html', context=context)

class AddStaff(LoginRequiredMixin, CreateView):
    template_name = 'management/staff_new.html'
    form_class = UserForm
    success_url = reverse_lazy('management:staff')
    queryset = User.objects.all()

    def form_valid(self, form):
        valid= super(AddStaff, self).form_valid(form)

        form.instance.set_password(form.instance.password)

        form.save()

        return valid
class StaffDetails(LoginRequiredMixin, DetailView):
    template_name = 'management/staff_details.html'
    model = User
    queryset = User.objects.all()
    pk_url_kwarg = 'id'


class ManagerView(LoginRequiredMixin, TemplateView):
    template_name = 'management/wards.html'

    def get_context_data(self, **kwargs):
        context = super(ManagerView, self).get_context_data(**kwargs)
        context['wards'] = Ward.objects.all()
        context['beds'] = Bed.objects.all()
        context['patients'] = Patient.objects.all()
        context['bills'] = DefaultBills.objects.all()
        context['request'] = Request.objects.all()
        return context


class AddWard(LoginRequiredMixin, RedirectView):
    url = reverse_lazy('management:wards')

    def post(self, request, *args, **kwargs):
        label= request.POST.get('label')

        Ward.objects.create(
            label=label,
            created_by=self.request.user
        )

        return super(AddWard, self).post(self,request,*args,**kwargs)

@login_required()
def ward_details(request, id):
    ward = Ward.objects.get(id=id)
    bed_number = request.POST.get('bed')

    errors = ''

    context = {
        'object': ward,
        'errors': ''
    }

    if request.method == 'POST':
        try:
            Bed.objects.get(number__exact=bed_number, ward=ward)
            errors = 'Bed has already been added'
            context = {
                'object': ward,
                'errors': errors,
            }
            return render(request=request, template_name='management/ward_details.html', context=context)
        except Bed.DoesNotExist:
            new_bed = Bed.objects.create(
                number=bed_number,
                ward=ward,
                status= 'Unassigned',
                created_by= request.user
            )
            ward.beds.add(new_bed)
            ward.save()
            return HttpResponseRedirect(reverse_lazy('management:ward-details', kwargs={'id': ward.id}))

    return render(request=request, template_name='management/ward_details.html', context=context)

class AddBill(LoginRequiredMixin, RedirectView):
    url = reverse_lazy('management:wards')

    def post(self, request, *args, **kwargs):
        bill_type = request.POST.get('bill_type')
        service = request.POST.get('service')
        amount = request.POST.get('amount')

        new_default_bill = DefaultBills.objects.create(
            bill_type = bill_type,
            service= service if service else '',
            amount=amount,
            created_by= self.request.user
        )

        return super(AddBill, self).post(self, request, *args, **kwargs)


class DelBill(LoginRequiredMixin, RedirectView):
    url = reverse_lazy('management:wards')

    def post(self, request, *args, **kwargs):
        bill_id = kwargs.get('bill_id')
        bill = DefaultBills.objects.get(id=bill_id)
        bill.delete()
        return super(DelBill, self).post(self, request, *args, **kwargs)


class UpdateBill(LoginRequiredMixin, RedirectView):
    url = reverse_lazy('management:wards')

    def post(self, request, *args, **kwargs):
        bill_id = kwargs.get('bill_id')
        amount = request.POST.get('amount')
        service = request.POST.get('service')
        bill_type = request.POST.get('bill_type')

        bill = DefaultBills.objects.get(id=bill_id)

        bill.amount = amount
        bill.service = service
        bill.bill_type = bill_type
        bill.save()

        return super(UpdateBill, self).post(self, request, *args, **kwargs)


@login_required()
def hr_view(request):
    complaints= Complaints.objects.all().exclude(status='Canceled').exclude(status='Resolved')
    com = Complaints.objects.filter(status='Resolved')


    context = {
        'complaints':complaints,
        'com':com
    }

    return render(request, 'management/hr.html', context)


@login_required()
def resolve_complaint(request, id):
    issue = Complaints.objects.get(id=id)
    context = {
        'issue':issue
    }
    if request.method == 'POST':
        issue.status = 'Resolved'
        issue.save()

    # return redirect('management:hr_view')
    return HttpResponseRedirect(reverse_lazy('management:hr_view'))
    # return render(request, 'management/hr.html', context)


@login_required()
def complaint_details(request,id):
    complaints = Complaints.objects.get(id=id)
    context = {
        'complaints':complaints
    }
    if not complaints.is_seen :
        complaints.is_seen = True
        complaints.seen_by = request.user
        complaints.seen_at = timezone.now()
        complaints.save()
    return render(request, 'management/response.html', context)


@login_required()
def response(request, id):
    complaint = Complaints.objects.get(id=id)
    review = request.POST.get('review')

    if request.method == 'POST':
        complaint.review = review
        complaint.review_by = request.user
        complaint.review_at = timezone.now()
        complaint.save()
    return HttpResponseRedirect(reverse_lazy('management:complaint_details', kwargs = {'id':id}))


class MakeRequest(LoginRequiredMixin, RedirectView):
    url = reverse_lazy('management:wards')

    def post(self, request, *args, **kwargs):
        department= request.POST.get('department')
        description= request.POST.get('description')

        new_request = Request.objects.create(
            department= department,
            description= description,
            status=0,
            created_by=self.request.user
        )

        return super(MakeRequest, self).post(self, request, *args, **kwargs)


class Requests(LoginRequiredMixin, ListView):
    template_name = 'management/requests.html'
    queryset = Request.objects.all()
    model = Request


class ChangeRequestStatus(LoginRequiredMixin, RedirectView):
    url = reverse_lazy('management:requests')

    def get(self, request, *args, **kwargs):
        request_id = kwargs.get('request_id')

        my_request = Request.objects.get(id=request_id)

        if my_request.status == 0:
            my_request.status = 1
            my_request.save()
        return super(ChangeRequestStatus, self).get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        request_id = kwargs.get('request_id')
        comment = request.POST.get('comment')

        try:
            my_request = Request.objects.get(id=request_id)
            if my_request.status == 0:
                my_request.comments = comment
                my_request.status = 2
                my_request.save()
        except Request.DoesNotExist:
            pass

        return super(ChangeRequestStatus, self).post(self, request, *args, **kwargs)

class Expenditures(LoginRequiredMixin, ListView):
    template_name = 'management/expenditure.html'
    queryset = Expenditure.objects.all()
    model = Expenditure

class AddMedicine(LoginRequiredMixin, RedirectView):
    url = reverse_lazy('management:expenditures')

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        medicine_type = request.POST.get('medicine_type')
        boxes_bought = request.POST.get('boxes_bought')
        pieces_per_box = request.POST.get('pieces_per_box')
        manufacturer = request.POST.get('manufacturer')
        manufacture_date = request.POST.get('manufacture_date')
        expiry_date = request.POST.get('expiry_date')
        pieces_selling_price = request.POST.get('piece_selling_price')
        pieces_cost_price = request.POST.get('piece_cost_price')

        if Medicine.objects.get(name__iexact=name):
            medicine = Medicine.objects.get(name__iexact=name)
            medicine.boxes_bought += boxes_bought
            medicine.boxes_left += boxes_bought
            medicine.pieces_per_boxes += pieces_per_box
            medicine.pieces += pieces_per_box * boxes_bought
            medicine.pieces_left += pieces_per_box * boxes_bought

            medicine.save()
        else:
            new_medicine = Medicine.objects.create(
                name=name,
                medicine_type=medicine_type,
                boxes_bought = boxes_bought,
                boxes_left = boxes_bought,
                pieces_per_box = pieces_per_box,
                pieces = pieces_per_box * boxes_bought,
                pieces_left= pieces_per_box * boxes_bought,
                manufacturer = manufacturer,
                manufacture_date= manufacture_date,
                expiry_date = expiry_date,
                pieces_selling_price=pieces_selling_price,
                created_by=self.request.user,
            )

        new exp = Expenditure.objects.create(
            category= Medicine,
            item=name,
            cost= pieces_cost_price
        )