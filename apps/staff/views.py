from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import datetime
from apps.management.models import LeavePeriod
from apps.staff.models import Leave, Staff
from apps.user.models import User
from.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, RedirectView, TemplateView
from django.utils import timezone
from django.urls import reverse_lazy


@login_required()
def dashboard(request):
    return render(request, 'staff/staff_dashboard.html')


@login_required()
def create_complaints(request):
    complaints = Complaints.objects.all()
    form = ComplaintForm
    context = {
        'complaints': complaints,
        'form': form,
    }
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.instance.status = 'Pending'
            form.instance.created_by = request.user
            form.save()
        return redirect('staff:create')
    return render(request, 'staff/complaints.html', context)


@login_required()
def cancel_complaint(request, id):
    complaint = Complaints.objects.get(id=id)

    context = {
        'complaint': complaint
    }

    if request.method == 'POST':
        complaint.status = 'Canceled'
        complaint.save()

    return redirect('staff:create')


# def new_leave(request):
#     leave = Leave.objects.all()
#     context = {
#         'leave': leave
#     }
#
#     start_date = request.POST.get('start_date')
#     end_date = request.POST.get('end_date')
#     # num_of_days = request.POST.get('num_of_days')
#     purpose = request.POST.get('purpose')
#
#     if request.method == 'POST':
#
#         new_one=Leave.objects.create(
#             start_date = start_date,
#             end_date = end_date,
#             purpose=purpose,
#             # num_of_days= (end_date - start_date).days,
#             status='Pending',
#             created_at=timezone.now().date(),
#             created_by=request.user
#         )
#         new_one.save()
#         return redirect('staff:dashboard')
#     return render(request, 'staff/add_new_leave.html', context)


def staff_leave_list(request):
    leaves = Leave.objects.filter(created_by=request.user)
    leave_year = Staff.objects.get(
        user=request.user,
        leave_period__end_date__year=timezone.now().year)

    context = {
        'leaves': leaves,
        'leave_year': leave_year
    }

    return render(request, 'staff/leave.html', context)


# def new_staff_leave(request):
#     new_leave = Leave.objects.all()
#     form = LeaveForm(req=request)
#
#     context = {
#         'new_leave': new_leave,
#         'form': form
#     }
#
#     if request.method == "POST":
#         form = LeaveForm(request.POST)
#         if form.is_valid():
#             staff = Staff.objects.get(user=request.user, leave_period__end_date__year=timezone.now().year)
#             form.instance.num_of_days = (form.instance.end_date - form.instance.start.date).days
#             form.instance.staff = staff
#             form.instance.status = 0
#             form.instance.created_by = request.user
#             staff.leaves.add(form.instance)
#             staff.save()
#             form.save()
#         return redirect('staff:leave-new')
#     return render(request, 'staff/add_new_leave.html', context)

class NewStaffLeave(LoginRequiredMixin, CreateView):
    success_url = reverse_lazy('staff:staff-leave-list')
    template_name = 'staff/add_new_leave.html'
    form_class = LeaveForm
    queryset = Leave.objects.all()

    def form_valid(self, form):
        valid = super(NewStaffLeave, self).form_valid(form)

        # current staff leave period for the user
        staff = Staff.objects.get(user=self.request.user, leave_period__end_date__year=timezone.now().year)

        # number of days to go on leave
        form.instance.num_of_days = (form.instance.end_date - form.instance.start_date).days

        # assigning staff object o leave.staff
        form.instance.staff = staff

        # setting leave status to Pending
        form.instance.status = 'Pending'

        form.instance.created_by = self.request.user

        # adding new leave record to staff object
        staff.leaves.add(form.instance)

        staff.save()

        form.save()

        return valid

    # this method allows us to pass self.request to the LeaveForm __init__() method
    def get_form_kwargs(self):
        kwargs = super(NewStaffLeave, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs