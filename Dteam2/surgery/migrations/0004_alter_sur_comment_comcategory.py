# Generated by Django 4.2.4 on 2023-08-12 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surgery', '0003_alter_sur_comment_comdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sur_comment',
            name='comCategory',
            field=models.CharField(choices=[('SUR', '수술 내역')], max_length=4),
        ),
    ]