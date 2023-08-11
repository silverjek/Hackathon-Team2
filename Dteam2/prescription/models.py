from django.db import models
from account.models import *
from medicalinfo.models import *
from diagnosis.models import *

# Create your models here.

class Prescription(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    info_id = models.ForeignKey(Medi_Info, on_delete=models.CASCADE)
    diag_id = models.ForeignKey(Diagnosis, on_delete=models.CASCADE)
    prePharm = models.CharField(max_length=100)
    preAddress = models.CharField(max_length=200)
    preDate = models.DateField()
    preChem = models.CharField(max_length=20)
    updateDate = models.DateTimeField(auto_now_add=True)

class Medication(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    info_id = models.ForeignKey(Medi_Info, on_delete=models.CASCADE)
    diag_id = models.ForeignKey(Diagnosis, on_delete=models.CASCADE)
    pre_id = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    mediName = models.CharField(max_length=100)
    mediEffect = models.CharField(max_length=300)
    mediDetail = models.CharField(max_length=100)
    mediCode = models.CharField(max_length=100)
    mediUnit = models.CharField(max_length=50)
    mediAmount = models.CharField(max_length=50)
    mediCount = models.CharField(max_length=50)
    mediPeriod = models.CharField(max_length=50)