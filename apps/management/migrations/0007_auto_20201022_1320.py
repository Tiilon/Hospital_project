# Generated by Django 3.1.2 on 2020-10-22 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
        ('management', '0006_auto_20201022_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='notes',
            field=models.ManyToManyField(blank=True, related_name='patient_notes', to='department.Note'),
        ),
        migrations.AlterField(
            model_name='bed',
            name='status',
            field=models.CharField(blank=True, choices=[('Assigned', 'Assigned'), ('Unassigned', 'Unassigned')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('Widowed', 'Widowed'), ('Married', 'Married'), ('Divorced', 'Divoreced'), ('Single', 'Single')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_type',
            field=models.CharField(blank=True, choices=[('ER', 'EMERGENCY'), ('OPD', 'OPD'), ('WARD', 'WARD')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='status',
            field=models.CharField(blank=True, choices=[('Canceled', 'Canceled'), ('Completed', 'Completed'), ('Pending', 'Pending')], max_length=100, null=True),
        ),
    ]