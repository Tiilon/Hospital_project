# Generated by Django 3.1.2 on 2020-11-11 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0007_auto_20201111_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescribedmedicine',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='prescribedmedicine',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='medicine_type',
            field=models.CharField(blank=True, choices=[('Tablet', 'Tablet'), ('Syrup', 'Syrup'), ('Capsule', 'Capsule')], max_length=100, null=True),
        ),
    ]
