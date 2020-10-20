# Generated by Django 3.1.2 on 2020-10-14 13:47

import apps.management.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='beds', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalDiagnosis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosis', models.CharField(blank=True, max_length=100, null=True)),
                ('is_admitted', models.BooleanField(blank=True, null=True)),
                ('onset', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='diagnosis', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'medical diagnosis',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(default=apps.management.models.generate, editable=False, max_length=100, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('patient_type', models.CharField(blank=True, choices=[('OPD', 'OPD'), ('WARD', 'WARD'), ('ER', 'EMERGENCY')], max_length=100, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True)),
                ('marital_status', models.CharField(blank=True, choices=[('Divorced', 'Divoreced'), ('Married', 'Married'), ('Single', 'Single'), ('Widowed', 'Widowed')], max_length=100, null=True)),
                ('date_of_birth', models.DateTimeField(blank=True, null=True)),
                ('admitted_at', models.DateTimeField(blank=True, null=True)),
                ('weight', models.CharField(blank=True, max_length=10, null=True)),
                ('bp', models.CharField(blank=True, max_length=100, null=True)),
                ('respiration', models.CharField(blank=True, max_length=100, null=True)),
                ('temperature', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patients', to=settings.AUTH_USER_MODEL)),
                ('diagnoses', models.ManyToManyField(blank=True, related_name='patient_diagnosis', to='management.MedicalDiagnosis')),
            ],
            options={
                'db_table': 'patient',
            },
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('beds', models.ManyToManyField(blank=True, related_name='ward_beds', to='management.Bed')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wards', to=settings.AUTH_USER_MODEL)),
                ('incharge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ward_incharge', to=settings.AUTH_USER_MODEL)),
                ('patients', models.ManyToManyField(blank=True, related_name='ward_patients', to='management.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treatment', models.CharField(blank=True, max_length=2000, null=True)),
                ('prescription', models.CharField(blank=True, max_length=2000, null=True)),
                ('status', models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Canceled', 'Canceled'), ('Completed', 'Completed')], max_length=100, null=True)),
                ('time_treated', models.TimeField(blank=True, null=True)),
                ('date_treated', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='treatments', to=settings.AUTH_USER_MODEL)),
                ('diagnosis', models.ForeignKey(blank='null', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='treatment_diagnosis', to='management.medicaldiagnosis')),
            ],
            options={
                'db_table': 'treatment',
            },
        ),
        migrations.AddField(
            model_name='medicaldiagnosis',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='diagnosis_patient', to='management.patient'),
        ),
        migrations.AddField(
            model_name='medicaldiagnosis',
            name='treatments',
            field=models.ManyToManyField(blank=True, related_name='diagnosis_treatments', to='management.Treatment'),
        ),
        migrations.AddField(
            model_name='bed',
            name='ward',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bed_ward', to='management.ward'),
        ),
    ]
