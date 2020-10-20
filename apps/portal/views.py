from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required
def portal_layout(request):
    return render(request=request, template_name='layout/portal_layout.html')

@login_required
def dashboard(request):
    return render(request=request, template_name='portal/portal_dashboard.html')