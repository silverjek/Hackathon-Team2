# Generated by Django 4.2.4 on 2023-08-12 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicalinfo', '0003_info_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info_comment',
            old_name='comCategery',
            new_name='comCategory',
        ),
    ]
