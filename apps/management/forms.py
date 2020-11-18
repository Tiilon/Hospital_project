import datetime

from django.forms import *
from apps.user.models import *
from .models import *


class UserForm(ModelForm):
    password = CharField(widget=PasswordInput(attrs={'required': True}), label = 'Password')

    class Meta:
        model= User
        fields = ('staff_id', 'first_name', 'last_name', 'user_type', 'role', 'password')

    def clean_staff_id(self):
        staff_id = self.cleaned_data.get('staff_id')

        try:
            User.objects.get(staff_id=staff_id)
            raise ValidationError('Staff with this staff id already exist')
        except User.DoesNotExist:
            pass

        return staff_id


class WardForm(ModelForm):

    class Meta:
        model = Ward
        fields = ('label', )


class LeavePeriodForm(ModelForm):
    class Meta:
        model = LeavePeriod
        fields = ('start_date', 'end_date', 'days_allowed')
        widgets = {
            'start_date': DateInput(attrs={'type': 'date', 'required': True}),
            'end_date': DateInput(attrs={'type': 'date', 'required': True})
        }

    def clean_end_date(self):
        end_date = self.cleaned_data.get('end_date')
        # convert end_date to a datetime type without the time data
        # Import datetime at the top
        # date1 = datetime.datetime.strptime(end_date, "%Y-%m-%d")

        # check if any leave period object does not match the end_date year of the new one
        try:
            LeavePeriod.objects.get(end_date__year=end_date.year)
            # raise error if try passes
            raise ValidationError('This Leave Period already exists')
        except LeavePeriod.DoesNotExist:
            pass

        return end_date


class RevenueForm(ModelForm):

    class Meta:
        model = Revenue
        fields = ('stream', 'description', 'amount')

        widgets = {
            'description': Textarea(attrs={'rows': 4})
        }

    STREAMS = {
        ("", '---------'),
        ('Donation', 'Donation'),
        ('Government', 'Government')
    }

    def __init__(self, *args, **kwargs):
        super(RevenueForm, self).__init__(*args, **kwargs)
        self.fields['stream'].choices = self.STREAMS