# Generated by Django 4.2.4 on 2023-08-12 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diagnosis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diag_Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comTitle', models.CharField(max_length=50)),
                ('comContent', models.TextField()),
                ('comDate', models.DateField(auto_now_add=True)),
                ('comCategory', models.CharField(choices=[('DIAG', '진단 내역')], max_length=4)),
                ('originPost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diagnosis.diagnosis')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]