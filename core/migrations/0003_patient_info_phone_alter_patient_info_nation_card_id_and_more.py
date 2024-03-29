# Generated by Django 4.1.2 on 2023-02-25 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_patient_info_admit_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_info',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='patient_info',
            name='Nation_Card_ID',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='patient_info',
            name='insurance_policy_ID',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
