# Generated by Django 3.0.4 on 2020-05-09 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0002_auto_20200509_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='FrequencyOfReoccurence',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='menu',
            name='isRecurring',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Vendor.Order'),
        ),
    ]
