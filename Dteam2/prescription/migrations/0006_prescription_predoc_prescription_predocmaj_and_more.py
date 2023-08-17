# Generated by Django 4.2.4 on 2023-08-17 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescription', '0005_pre_comment_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='preDoc',
            field=models.CharField(default='김멋사', max_length=50),
        ),
        migrations.AddField(
            model_name='prescription',
            name='preDocMaj',
            field=models.CharField(default='외과 전문의', max_length=50),
        ),
        migrations.AddField(
            model_name='prescription',
            name='preHospital',
            field=models.CharField(default='멋사 병원', max_length=50),
        ),
    ]
