# Generated by Django 4.2.4 on 2023-08-12 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surgery', '0002_sur_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sur_comment',
            name='comDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]