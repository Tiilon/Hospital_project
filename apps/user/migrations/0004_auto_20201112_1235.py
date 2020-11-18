# Generated by Django 3.1.2 on 2020-11-12 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20201110_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('NRS', 'Nurse'), ('Acc', 'Accountant'), ('IT', 'IT'), ('HR', 'Human Resource'), ('DR', 'Doctor'), ('PHM', 'Pharmacist'), ('HM', 'Hospital Manager'), ('CH', 'Cashier')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(blank=True, choices=[('Active', 'Active'), ('Dismissed', 'Dismissed'), ('Leave', 'Leave'), ('Suspended', 'Suspended')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(blank=True, choices=[('NU', 'Normal Staff'), ('AD', 'Administrator'), ('MU', 'Manager'), ('SU', 'Support')], max_length=255, null=True),
        ),
    ]
