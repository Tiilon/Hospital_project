# Generated by Django 3.1.2 on 2020-11-12 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_auto_20201112_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='leave',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='leave',
            name='status',
            field=models.CharField(blank=True, choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Rejected', 'Rejected')], max_length=100, null=True),
        ),
    ]
