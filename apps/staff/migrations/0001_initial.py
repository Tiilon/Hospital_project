# Generated by Django 3.1.2 on 2020-11-10 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('management', '0026_auto_20201110_1123'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(default=django.utils.timezone.now)),
                ('num_of_days', models.IntegerField(default=0)),
                ('status', models.CharField(blank=True, choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Rejected', 'Rejected')], max_length=100, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leaves', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'leave',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_days', models.IntegerField(default=0)),
                ('no_days_used', models.IntegerField(default=0)),
                ('no_days_left', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='staffs', to=settings.AUTH_USER_MODEL)),
                ('leave_period', models.ForeignKey(blank='null', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='staff_leave_period', to='management.leaveperiod')),
                ('leaves', models.ManyToManyField(blank=True, related_name='staff_leaves', to='staff.Leave')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='staff', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'staff',
            },
        ),
        migrations.AddField(
            model_name='leave',
            name='staff',
            field=models.ForeignKey(blank='null', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leave_staff', to='staff.staff'),
        ),
    ]
