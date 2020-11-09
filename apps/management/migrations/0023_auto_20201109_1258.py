# Generated by Django 3.1.2 on 2020-11-09 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0022_auto_20201109_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, choices=[('Female', 'Female'), ('Male', 'Male')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('Divorced', 'Divoreced'), ('Single', 'Single'), ('Married', 'Married'), ('Widowed', 'Widowed')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_type',
            field=models.CharField(blank=True, choices=[('Ward', 'Ward'), ('DISCHARGED', 'DISCHARGED'), ('ER', 'EMERGENCY'), ('OPD', 'OPD')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='department',
            field=models.CharField(blank=True, choices=[('HR', 'Human Resource'), ('Account', 'Account'), ('Ward', 'Ward'), ('Management', 'Management'), ('Pharmacy', 'Pharmacy')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, 'Accepted'), (2, 'Rejected'), (0, 'Pending')], null=True),
        ),
    ]
