# Generated by Django 4.2.4 on 2023-08-17 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosis', '0004_diag_comment_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosis',
            name='diagHospital',
            field=models.CharField(blank=True, default='hospital', max_length=50, null=True),
        ),
    ]