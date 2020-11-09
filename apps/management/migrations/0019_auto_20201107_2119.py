# Generated by Django 3.1.2 on 2020-11-07 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0018_auto_20201107_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='status',
            field=models.CharField(blank=True, choices=[('Canceled', 'Canceled'), ('Resolved', 'Resolved'), ('Pending', 'Pending')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, choices=[('Female', 'Female'), ('Male', 'Male')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('Married', 'Married'), ('Widowed', 'Widowed'), ('Single', 'Single'), ('Divorced', 'Divoreced')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_type',
            field=models.CharField(blank=True, choices=[('Ward', 'Ward'), ('DISCHARGED', 'DISCHARGED'), ('OPD', 'OPD'), ('ER', 'EMERGENCY')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='status',
            field=models.CharField(blank=True, choices=[('Canceled', 'Canceled'), ('Completed', 'Completed'), ('Pending', 'Pending')], max_length=100, null=True),
        ),
    ]