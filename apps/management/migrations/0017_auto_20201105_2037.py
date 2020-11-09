# Generated by Django 3.1.2 on 2020-11-05 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0016_auto_20201105_1912'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='complaints',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AlterField(
            model_name='complaints',
            name='status',
            field=models.CharField(blank=True, choices=[('Canceled', 'Canceled'), ('Seen', 'Seen'), ('Pending', 'Pending'), ('Resolved', 'Resolved')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('Married', 'Married'), ('Widowed', 'Widowed'), ('Single', 'Single'), ('Divorced', 'Divoreced')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_type',
            field=models.CharField(blank=True, choices=[('Ward', 'Ward'), ('DISCHARGED', 'DISCHARGED'), ('ER', 'EMERGENCY'), ('OPD', 'OPD')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='status',
            field=models.CharField(blank=True, choices=[('Canceled', 'Canceled'), ('Pending', 'Pending'), ('Completed', 'Completed')], max_length=100, null=True),
        ),
    ]