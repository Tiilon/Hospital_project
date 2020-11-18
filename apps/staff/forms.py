from django.forms import *
from apps.management.models import *
from .models import *


class ComplaintForm(ModelForm):
    class Meta:
        model = Complaints
        fields ={
            ('complaints'),
        }
        widgets = {
            'complaints': Textarea(attrs={'required': True, 'rows': 1, 'placeholder': 'Type your complaints here...', 'autofocus': True, 'class': 'form-control border-0'})
                    }


class LeaveForm(ModelForm):
    class Meta:
        model = Leave
        fields = (
            'start_date',
            'end_date',
            'purpose'
        )

        widgets = {
            'start_date': DateInput(attrs={'type': 'date', 'required':True}),
            'end_date': DateInput(attrs={'type': 'date', 'required':True}),
            'purpose': Textarea(attrs={'cols': 3})
        }

    def __init__(self, request=None, *args, **kwargs):
        super(LeaveForm, self).__init__(*args,**kwargs)
        self.request = request

    def clean(self):
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')

        num_of_days = (end_date-start_date).days

        staff = Staff.objects.get(user = self.request.user, leave_period__end_date__year=timezone.now().year)

        if end_date < start_date:
            raise ValidationError("End date is before Start date selected")

        if end_date == start_date:
            raise ValidationError("Start date cannot be before End date")

        if staff.no_days_left < num_of_days:
            raise ValidationError('Number of days selected exceeds your days remaining')

        return self.cleaned_data