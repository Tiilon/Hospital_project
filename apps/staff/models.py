from django.conf import settings
from django.db import models

# Create your models here.
from django.utils import timezone


class Staff(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='staff', blank=True, null=True)
    total_days = models.IntegerField(default=0)
    no_days_used = models.IntegerField(default=0)
    no_days_left = models.IntegerField(default=0)
    leaves = models.ManyToManyField('Leave', related_name='staff_leaves', blank=True)
    leave_period = models.ForeignKey('management.LeavePeriod', on_delete=models.SET_NULL, related_name='staff_leave_period', blank='null', null=True)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='staffs', blank=True, null=True)

    def __str__(self):
        return f"{self.user}"

    class Meta:
        db_table = 'staff'
        get_latest_by = 'created_at'


LEAVE_STATUS = {
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected'),
}


class Leave(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, related_name='leave_staff', blank='null', null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    purpose = models.CharField(max_length=300, blank=True, null=True)
    num_of_days = models.IntegerField(default=0)
    status = models.CharField(max_length=100, null=True, blank=True, choices=LEAVE_STATUS)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='leaves', blank=True, null=True)

    def __str__(self):
        return f"{self.num_of_days}"

    class Meta:
        db_table = 'leave'
