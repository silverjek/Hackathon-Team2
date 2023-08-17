# Generated by Django 4.2.4 on 2023-08-17 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosis', '0007_diagnosis_diagdocmaj_alter_diagnosis_diagdoc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosis',
            name='diagChart',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='diagCount',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='diagHosAddrss',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='diagHosType',
            field=models.CharField(default='의원', max_length=30),
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='diagLtVisit',
            field=models.DateField(blank=True, null=True),
        ),
    ]
