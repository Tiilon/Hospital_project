# Generated by Django 3.1.2 on 2020-11-10 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
        ('management', '0026_auto_20201110_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaveperiod',
            name='staff',
            field=models.ManyToManyField(blank='null', related_name='staff', to='staff.Staff'),
        ),
    ]