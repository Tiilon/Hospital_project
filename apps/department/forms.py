from django.forms import *
from apps.management import models
from apps.portal.models import DefaultBills


class NewPatientForm(ModelForm):

    class Meta:
        model = models.Patient
        fields = (
            'first_name',
            'last_name',
            'gender',
            'marital_status',
            'date_of_birth',
        )
        widgets = {
            'date_of_birth': TextInput(attrs={
                'type': 'date'
            })
        }

    def clean(self):
        try:
            card_charge = DefaultBills.objects.get(bill_type='CB')
        except DefaultBills.DoesNotExist:
            raise ValidationError(
                message= 'There is no card bills in the system'
            )
        return self.cleaned_data
