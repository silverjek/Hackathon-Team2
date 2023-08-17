# Generated by Django 4.2.4 on 2023-08-17 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosis', '0005_diagnosis_diaghospital'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosis',
            name='diagDoc',
            field=models.CharField(default='의사이름', max_length=20),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='diagHospital',
            field=models.CharField(default='병원명', max_length=50),
        ),
    ]
