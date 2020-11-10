# Generated by Django 3.1.2 on 2020-11-10 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0003_auto_20201109_1634'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicine',
            old_name='piece_selling_price',
            new_name='cost_price_per_box',
        ),
        migrations.RemoveField(
            model_name='medicine',
            name='boxes_sold',
        ),
        migrations.RemoveField(
            model_name='medicine',
            name='pieces',
        ),
        migrations.RemoveField(
            model_name='medicine',
            name='pieces_left',
        ),
        migrations.RemoveField(
            model_name='medicine',
            name='pieces_per_boxes',
        ),
        migrations.RemoveField(
            model_name='medicine',
            name='pieces_sold',
        ),
        migrations.AddField(
            model_name='medicine',
            name='cost_price_per_unit',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='medicine',
            name='no_in_box',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='medicine',
            name='selling_price_per_box',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='medicine',
            name='selling_price_per_unit',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='medicine',
            name='sold_boxes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='medicine',
            name='sold_units',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='medicine',
            name='total_cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='medicine',
            name='total_no_units_accumulated',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='medicine',
            name='total_sales',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='medicine',
            name='units_left',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='boxes_bought',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='boxes_left',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='medicine_type',
            field=models.CharField(blank=True, choices=[('Capsule', 'Capsule'), ('Tablet', 'Tablet'), ('Syrup', 'Syrup')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, 'Paid'), (0, 'Not paid')], null=True),
        ),
    ]
