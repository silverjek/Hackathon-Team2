# Generated by Django 4.2.4 on 2023-08-12 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalinfo', '0004_rename_comcategery_info_comment_comcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info_comment',
            name='comCategory',
            field=models.CharField(choices=[('INFO', '의료 정보')], max_length=4),
        ),
    ]
