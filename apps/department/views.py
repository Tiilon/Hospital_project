from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

@login_required()
def dept_dashboard(request):
    return render(request=request, template_name='department/dept_dashboard.html')