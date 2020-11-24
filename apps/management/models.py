from random import randrange
from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.


class Ward(models.Model):
    label = models.CharField(max_length=100, blank=True, null=True)
    incharge = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='ward_incharge', blank=True, null=True)
    beds= models.ManyToManyField('Bed', related_name='ward_beds', blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='wards', blank=True, null=True)
    patients= models.ManyToManyField('Patient', related_name='ward_patients', blank=True)

    def __str__(self):
        return self.label

    class meta:
        db_table= 'ward'


BED_STATUS = {
    ('Assigned', 'Assigned'),
    ('Unassigned', 'Unassigned')
}


class Bed(models.Model):
    number = models.CharField(max_length=200, blank=True, null=True)
    ward = models.ForeignKey(Ward, on_delete=models.SET_NULL, related_name='bed_ward',blank=True, null=True)
    status = models.CharField(max_length=200,blank=True, null=True, choices=BED_STATUS)
    allocate = models.ForeignKey('BedAllocate', on_delete=models.SET_NULL, related_name='bed_allocate', blank=True, null=True)
    bed_allocates = models.ManyToManyField('BedAllocate',  related_name='bed_bed_allocate', blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='beds', blank=True, null=True)

    def __str__(self):
        return self.number

    class Meta:
        db_table = 'bed'
        ordering = ('number',)


class BedAllocate(models.Model):
    bed = models.ForeignKey(Bed, related_name='bed_allocate_bed', blank='True', null=True, on_delete=models.SET_NULL)
    patient = models.ForeignKey('Patient', related_name='bed_allocate_patient', null=True, blank=True, on_delete=models.SET_NULL)
    date_admitted = models.DateField(blank=True, null=True)
    time_admitted = models.TimeField(blank=True, null=True)
    time_discharged = models.TimeField(blank=True, null=True)
    date_discharged = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='bed_allocates', blank=True, null=True)

    def __str__(self):
        return f"{self.bed} - {self.patient}"

    class Meta:
        db_table = 'bed_allocate'


def generate():
    FROM = '0123456789'
    LENGTH = 10
    pat_id = ""
    for i in range(LENGTH):
        pat_id += FROM[randrange(0, len(FROM))]

    return f"PT{pat_id}/{timezone.now().year}"


GENDER = {
    ('Male', 'Male'),
    ('Female', 'Female'),
}

PATIENT_TYPE = {
    ('OPD', 'OPD'),
    ('Ward', 'Ward'),
    ('ER', 'EMERGENCY'),
    ('DISCHARGED', 'DISCHARGED')
}


MARITAL = {
    ('Married', 'Married'),
    ('Single', 'Single'),
    ('Divorced', 'Divorced'),
    ('Widowed', 'Widowed'),
}


class VitalSign(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.SET_NULL, blank=True, null=True, related_name='vital_sign_patient')
    time = models.TimeField(default=timezone.now)
    weight = models.DecimalField( max_digits=10, decimal_places=2,blank=True, null=True)
    diastolic = models.IntegerField( blank=True, null=True)
    pulse = models.IntegerField(blank=True, null=True)
    systolic = models.IntegerField( blank=True, null=True)
    respiration = models.IntegerField( blank=True, null=True)
    temperature = models.DecimalField( max_digits=10, decimal_places=2,blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, related_name='vital_signs')

    class Meta:
        db_table = 'vital_sign'
        ordering = ('-time',)

    def __str__(self):
        return f"{self.patient.full_name()}-{self.time}"


class Patient(models.Model):
    patient_id = models.CharField(default=generate, unique=True, editable=False, max_length=100)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    patient_type = models.CharField(max_length=100, blank=True, null=True, choices=PATIENT_TYPE)
    gender = models.CharField(max_length=100, blank=True, null=True, choices=GENDER)
    marital_status = models.CharField(max_length=100,blank=True,null=True,choices=MARITAL)
    date_of_birth = models.DateField(blank=True, null=True)
    date_admitted = models.DateField(blank=True, null=True)
    time_admitted = models.TimeField(blank=True, null=True)
    time_discharged = models.TimeField(blank=True, null=True)
    date_discharged = models.DateField(blank=True, null=True)
    bed = models.ForeignKey(Bed, on_delete=models.SET_NULL, related_name='patient_bed', blank=True, null=True)
    vital_signs = models.ManyToManyField(VitalSign, related_name='patient_vital_signs', blank=True)
    discharged_at = models.DateTimeField(blank=True, null=True)
    diagnoses = models.ManyToManyField('MedicalDiagnosis', related_name='patient_diagnosis', blank=True)
    notes = models.ManyToManyField('department.Note', related_name='patient_notes', blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='patients', blank=True, null=True)

    def __str__(self):
        return self.patient_id

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'patient'


class MedicalDiagnosis(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, related_name='diagnosis_patient', blank=True, null=True)
    complaints = models.CharField(max_length=1000, blank=True, null=True)
    symptoms = models.CharField(max_length=2000, blank=True, null=True)
    diagnosis = models.CharField(max_length=100,blank=True, null=True)
    is_admitted = models.BooleanField(blank=True,null=True)
    onset = models.CharField(max_length=100, blank=True, null=True)
    treatments = models.ManyToManyField('Treatment', related_name='diagnosis_treatments', blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='diagnosis', blank=True, null=True)

    def __str__(self):
        return self.diagnosis

    class Meta:
        db_table= 'medical diagnosis'
        ordering = ('-created_at',)


TREATMENT_STATUS = {
    ('Pending', 'Pending'),
    ('Canceled','Canceled'),
    ('Completed', 'Completed'),
}


class Treatment(models.Model):
    diagnosis = models.ForeignKey(MedicalDiagnosis, on_delete=models.SET_NULL, related_name='treatment_diagnosis', blank='null', null=True)
    treatment = models.CharField(max_length=2000, blank=True, null=True)
    prescription = models.CharField(max_length=2000, blank=True,null=True)
    pharmacy_prescription = models.ForeignKey('pharmacy.Prescription', on_delete= models.SET_NULL, related_name='treatment_prescription', blank=True, null=True)
    status = models.CharField(max_length=100,blank=True,null=True, choices= TREATMENT_STATUS)
    time_treated = models.TimeField(blank=True, null=True)
    date_treated= models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='treatments',blank=True, null=True)

    def __str__(self):
        return str(self.treatment) + ' - ' + str(self.prescription)

    class Meta:
        db_table = 'treatment'
        ordering = ('-created_at',)


COMPLAINTS_STATUS = {
    ('Pending', 'Pending'),
    ('Resolved', 'Resolved'),
    ('Canceled', 'Canceled'),

}


class Complaints(models.Model):
    complaints = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='complaints', blank=False, null=True)
    review = models.CharField(max_length=3000, blank=True, null=True)
    is_seen = models.BooleanField(blank=True, null=True, default=False)
    seen_at = models.DateTimeField(blank=True, null=True)
    seen_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='complaint_seen', blank=False, null=True)
    status = models.CharField(max_length=200, blank=True, null=True, choices=COMPLAINTS_STATUS)
    review_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='complaint_review',blank=False, null=True)
    review_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ('-created_at',)
        db_table = 'complaint'

    def __str__(self):
        return str(self.complaints)


DEPARTMENTS ={
    ('Ward', 'Ward'),
    ('Pharmacy', 'Pharmacy'),
    ('Account', 'Account'),
    ('Management', 'Management'),
    ('HR', 'Human Resource')
}

REQUEST_STATUS = {
    (0, 'Pending'),
    (1, 'Accepted'),
    (2, 'Rejected')
}


class Request(models.Model):
    department = models.CharField(max_length=200, blank=True, null=True, choices=DEPARTMENTS)
    description = models.TextField(max_length=5000, blank=True, null=True)
    status = models.IntegerField(blank=True, null= True, choices=REQUEST_STATUS)
    comments = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='requests', blank=True, null=True)

    def __str__(self):
        return str(self.department)

    class Meta:
        db_table = 'request'


class Expenditure(models.Model):
    category = models.CharField(max_length=100, blank=True, null=True)
    item = models.CharField(max_length=300, blank=True, null=True)
    total_cost = models.DecimalField(max_digits=10, blank=True, null=True, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='expenditures', blank=True, null=True)

    def __str__(self):
        return f"{self.category} - {self.total_cost}"

    class Meta:
        db_table = 'expenditure'


class LeavePeriod(models.Model):
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    num_of_days = models.IntegerField(default=0)
    days_allowed = models.IntegerField(default=0)
    staffs = models.ManyToManyField('staff.Staff', related_name='staff', blank='null')
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='leave_periods', blank=True, null=True)

    def __str__(self):
        return f"{self.start_date}-{self.end_date}"

    class Meta:
        db_table = 'leave_period'


STREAMS = {
    ('Government', 'Government'),
    ('Patient', 'Patient'),
    ('Donation', 'Donation')
}


class Revenue(models.Model):
    stream = models.CharField(max_length=200, blank=True, null=True, choices=STREAMS)
    bill = models.ForeignKey('portal.Bill', related_name='revenue_bill', on_delete=models.SET_NULL, blank=True, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, related_name='revenue_patient', blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, related_name='revenues')

    def __str__(self):
        return str(self.stream)

    class Meta:
        db_table = 'revenue'
        ordering = ('-created_at',)


A_STATUS = {
    ('Show', 'Show'),
    ('Hide', 'Hide')
}


# class Announcement(models.Model):
#     message = models.CharField(max_length=200, blank=True, null=True)
#     title = models.CharField(max_length=200, blank=True, null=True)
#     status = models.CharField(max_length=200, blank=True, null=True, choices=A_STATUS)