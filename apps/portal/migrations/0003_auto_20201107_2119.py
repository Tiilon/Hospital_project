# Generated by Django 3.1.2 on 2020-11-07 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_auto_20201103_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_type',
            field=models.CharField(blank=True, choices=[('CB', 'Card Bills'), ('PhB', 'Pharmacy Bills'), ('PB', 'Procedure Bills'), ('WB', 'Ward Bills'), ('LB', 'Lab Bills'), ('CnB', 'Consultation Bill')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Not Paid'), (1, 'Paid')], null=True),
        ),
        migrations.AlterField(
            model_name='defaultbills',
            name='bill_type',
            field=models.CharField(blank=True, choices=[('CB', 'Card Bills'), ('PhB', 'Pharmacy Bills'), ('PB', 'Procedure Bills'), ('WB', 'Ward Bills'), ('LB', 'Lab Bills'), ('CnB', 'Consultation Bill')], max_length=100, null=True),
        ),
    ]
