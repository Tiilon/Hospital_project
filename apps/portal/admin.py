from django.contrib import admin

# Register your models here.
from apps.portal.models import Bill, DefaultBills

admin.site.register(Bill)
admin.site.register(DefaultBills)