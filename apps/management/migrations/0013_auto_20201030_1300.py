# Generated by Django 3.1.2 on 2020-10-30 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0012_auto_20201027_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('Divorced', 'Divoreced'), ('Widowed', 'Widowed'), ('Single', 'Single'), ('Married', 'Married')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_type',
            field=models.CharField(blank=True, choices=[('Ward', 'Ward'), ('OPD', 'OPD'), ('ER', 'EMERGENCY')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='status',
            field=models.CharField(blank=True, choices=[('Canceled', 'Canceled'), ('Pending', 'Pending'), ('Completed', 'Completed')], max_length=100, null=True),
        ),
    ]
