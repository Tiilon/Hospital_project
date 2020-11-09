from django.forms import *
from apps.management.models import Complaints


class ComplaintForm(ModelForm):
    class Meta:
        model = Complaints
        fields ={
            ('complaints'),
        }
        widgets = {
            'complaints': Textarea(attrs={'required': True, 'rows': 1, 'placeholder': 'Type your complaints here...', 'autofocus': True, 'class': 'form-control border-0'})
        }