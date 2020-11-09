from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
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