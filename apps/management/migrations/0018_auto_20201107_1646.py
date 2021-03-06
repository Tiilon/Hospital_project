# Generated by Django 3.1.2 on 2020-11-07 16:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('management', '0017_auto_20201105_2037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaints',
            old_name='response',
            new_name='review',
        ),
        migrations.AddField(
            model_name='complaints',
            name='is_seen',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='complaints',
            name='review_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='complaints',
            name='review_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='complaint_review', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='complaints',
            name='seen_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='complaints',
            name='seen_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='complaint_seen', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='status',
            field=models.CharField(blank=True, choices=[('Resolved', 'Resolved'), ('Seen', 'Seen'), ('Canceled', 'Canceled'), ('Pending', 'Pending')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('Married', 'Married'), ('Divorced', 'Divoreced'), ('Single', 'Single'), ('Widowed', 'Widowed')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_type',
            field=models.CharField(blank=True, choices=[('ER', 'EMERGENCY'), ('Ward', 'Ward'), ('DISCHARGED', 'DISCHARGED'), ('OPD', 'OPD')], max_length=100, null=True),
        ),
        migrations.AlterModelTable(
            name='complaints',
            table='complaint',
        ),
    ]
