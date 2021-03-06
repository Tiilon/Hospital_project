# Generated by Django 3.1.2 on 2020-10-27 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0011_auto_20201027_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='bed',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patient_bed', to='management.bed'),
        ),
        migrations.AddField(
            model_name='patient',
            name='date_discharged',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bed',
            name='status',
            field=models.CharField(blank=True, choices=[('Unassigned', 'Unassigned'), ('Assigned', 'Assigned')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('Married', 'Married'), ('Single', 'Single'), ('Divorced', 'Divoreced'), ('Widowed', 'Widowed')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_type',
            field=models.CharField(blank=True, choices=[('WARD', 'WARD'), ('OPD', 'OPD'), ('ER', 'EMERGENCY')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='status',
            field=models.CharField(blank=True, choices=[('Canceled', 'Canceled'), ('Completed', 'Completed'), ('Pending', 'Pending')], max_length=100, null=True),
        ),
    ]
