# Generated by Django 3.1.2 on 2020-11-09 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0002_auto_20201109_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='pieces',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='medicine',
            name='pieces_left',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='medicine_type',
            field=models.CharField(blank=True, choices=[('Syrup', 'Syrup'), ('Capsule', 'Capsule'), ('Tablet', 'Tablet')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Not paid'), (1, 'Paid')], null=True),
        ),
    ]
