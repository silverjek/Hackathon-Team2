from django.db import models
from account.models import *
from medicalinfo.models import *

# Create your models here.

class Diagnosis(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    info_id = models.ForeignKey(Medi_Info, on_delete=models.CASCADE)
    diagDate = models.DateField()
    diagRegi = models.CharField(max_length=50)
    diagNum = models.CharField(max_length=50)
    diagMajor = models.CharField(max_length=100)
    diagMajCode = models.CharField(max_length=100)
    diagTF = models.BooleanField(default=False) #False-임상적 추정 / True-최종 진단
    diagMinor = models.CharField(max_length=300)
    diagMinCode = models.CharField(max_length=300)
    diagInitDate = models.DateField()
    diagMemo = models.TextField(null=False, blank=False, default='')
    diagIn = models.DateField()
    diagOut = models.DateField()
    diagUSage = models.CharField(max_length=50, blank=True, null=True)
    diagETC = models.TextField(null=False, blank=False, default='') 
    updateDate = models.DateTimeField(auto_now_add=True)