from django.conf import settings
from django.db import models

# Create your models here.
from django.utils import timezone

MEDICINE_TYPE ={
    ('Syrup', 'Syrup'),
    ('Capsule', 'Capsule'),
    ('Tablet', 'Tablet'),
}
class Medicine(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    medicine_type = models.CharField(max_length=100, blank=True, null=True, choices=MEDICINE_TYPE)
    boxes_bought = models.IntegerField(blank=True, null=True, default=0)
    boxes_left = models.IntegerField(blank=True, null=True, default=0)
    boxes_sold = models.IntegerField(blank=True, null=True, default=0)
    pieces_per_boxes = models.IntegerField(blank=True, null=True, default=0)
    pieces_left = models.IntegerField(blank=True, null=True, default=0)
    pieces_sold = models.IntegerField(blank=True, null=True, default=0)
    pieces = models.IntegerField(blank=True, null=True, default=0)
    expiry_date = models.DateField(blank=True, null=True)
    manufacture_date = models.DateField(blank=True, null=True)
    manufacturer = models.CharField(max_length=200, blank=True, null=True)
    piece_selling_price = models.DecimalField(decimal_places=2,max_digits=10,blank=True,null=True)
    piece_cost_price = models.DecimalField(decimal_places=2,max_digits=10,blank=True,null=True)
    prescribed_medicines = models.ManyToManyField('PrescribedMedicine', related_name='medicine_prescribed_medicines', blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='medicines', blank=True, null=True)


    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = 'medicine'


class PrescribedMedicine(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.SET_NULL, related_name='prescribed_medicine_medicine',blank=True,null=True)
    prescription = models.ForeignKey('Prescription', on_delete=models.SET_NULL, related_name='prescribed_medicine_prescribed',blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='prescribed_medicines', blank=True, null=True)

    def __str__(self):
        return str(self.medicine.name)

    class Meta:
        db_table ='prescibed_medicine'


PRE_STATUS = {
  (1, 'Paid'),
  (0, 'Not paid')
}


class Prescription(models.Model):
    prescription_id = models.CharField(max_length=200,blank=True,null=True)
    medicines = models.ManyToManyField(PrescribedMedicine, related_name='prescription_medicine', blank=True)
    dosage = models.CharField(max_length=2000, blank=True, null=True)
    frequency = models.CharField(max_length=200,blank=True,null=True)
    patient = models.ForeignKey('management.Patient', on_delete=models.SET_NULL, related_name='prescription_patient', blank=True,null=True)
    treatment = models.ForeignKey('management.Treatment',on_delete=models.SET_NULL, related_name='prescription_treatment', blank=True,null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True, choices=PRE_STATUS)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='prescriptions', blank=True, null=True)

    def __str__(self):
        return str(self.prescription_id)

    class Meta:
        db_table = 'prescription'
