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

class Pre_Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    originPost = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='replies')
    #user_type = models.ForeignKey(User.userType, on_delete=models.CASCADE)
    #user_name = models.ForeignKey(User.username, on_delete=models.CASCADE) 이름 어케 받을지 유저 모델과 함께 생각해보기
    
    comTitle = models.CharField(max_length=50)
    comContent = models.TextField()
    comDate = models.DateTimeField(auto_now_add=True)

    CATEGORY_CHOICES=(
        ('PRE','처방 내역'),
    )
    comCategory = models.CharField(max_length=4, choices=CATEGORY_CHOICES)
    
    def user_name(self):
        return self.user_id.userFullName

    def user_type(self):
        return self.user_id.userType