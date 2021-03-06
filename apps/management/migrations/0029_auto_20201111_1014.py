# Generated by Django 3.1.2 on 2020-11-11 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0028_auto_20201110_1432'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leaveperiod',
            old_name='staff',
            new_name='staffs',
        ),
        migrations.AlterField(
            model_name='bed',
            name='status',
            field=models.CharField(blank=True, choices=[('Unassigned', 'Unassigned'), ('Assigned', 'Assigned')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='status',
            field=models.CharField(blank=True, choices=[('Resolved', 'Resolved'), ('Pending', 'Pending'), ('Canceled', 'Canceled')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('Married', 'Married'), ('Widowed', 'Widowed'), ('Single', 'Single'), ('Divorced', 'Divoreced')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_type',
            field=models.CharField(blank=True, choices=[('OPD', 'OPD'), ('DISCHARGED', 'DISCHARGED'), ('ER', 'EMERGENCY'), ('Ward', 'Ward')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='department',
            field=models.CharField(blank=True, choices=[('HR', 'Human Resource'), ('Account', 'Account'), ('Ward', 'Ward'), ('Management', 'Management'), ('Pharmacy', 'Pharmacy')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, 'Accepted'), (0, 'Pending'), (2, 'Rejected')], null=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='status',
            field=models.CharField(blank=True, choices=[('Completed', 'Completed'), ('Pending', 'Pending'), ('Canceled', 'Canceled')], max_length=100, null=True),
        ),
    ]
