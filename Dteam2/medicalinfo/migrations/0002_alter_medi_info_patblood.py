# Generated by Django 4.2.4 on 2023-08-10 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medi_info',
            name='patBlood',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('O', 'O'), ('AB', 'AB')], max_length=2),
        ),
    ]
