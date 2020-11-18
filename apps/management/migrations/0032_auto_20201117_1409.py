# Generated by Django 3.1.2 on 2020-11-17 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portal', '0006_auto_20201117_1409'),
        ('management', '0031_auto_20201112_1235'),
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
            field=models.CharField(blank=True, choices=[('Widowed', 'Widowed'), ('Married', 'Married'), ('Single', 'Single'), ('Divorced', 'Divorced')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_type',
            field=models.CharField(blank=True, choices=[('DISCHARGED', 'DISCHARGED'), ('OPD', 'OPD'), ('ER', 'EMERGENCY'), ('Ward', 'Ward')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='department',
            field=models.CharField(blank=True, choices=[('Ward', 'Ward'), ('Pharmacy', 'Pharmacy'), ('Account', 'Account'), ('HR', 'Human Resource'), ('Management', 'Management')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Pending'), (1, 'Accepted'), (2, 'Rejected')], null=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='status',
            field=models.CharField(blank=True, choices=[('Completed', 'Completed'), ('Pending', 'Pending'), ('Canceled', 'Canceled')], max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Revenue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stream', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('bill', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='revenue_bill', to='portal.bill')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='revenues', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='revenue_patient', to='management.patient')),
            ],
            options={
                'db_table': 'revenue',
                'ordering': ('-created_at',),
            },
        ),
    ]