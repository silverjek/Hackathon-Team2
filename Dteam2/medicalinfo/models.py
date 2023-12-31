from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from account.models import *

# Create your models here.

class Medi_Info(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    patName = models.CharField(max_length=30)
    SEX_CHOICES=(
        ('FEMALE','Female'),
        ('MALE','Male')
    )
    patSex = models.CharField(max_length=6, choices=SEX_CHOICES)
    patBirth = models.DateField()
    patAge = models.IntegerField(default=0)
    patAddress = models.CharField(max_length=200)
    patSSN = models.CharField(max_length=14)
    BLOOD_CHOICES=(
        ('A','A'),
        ('B','B'),
        ('O','O'),
        ('AB','AB')
    )
    patBlood = models.CharField(max_length=2, choices=BLOOD_CHOICES)
    RH_CHOICES=(
        ('PLUS','+'),
        ('MINUS','-')
    )
    patRH = models.CharField(max_length=5, choices=RH_CHOICES)
    patHeight = models.FloatField()
    patWeight = models.FloatField()
    patPhone = models.CharField(max_length=13, default='010-1234-5678')
    updateDate = models.DateTimeField(auto_now_add=True)
    doc=models.CharField(max_length=50, default='김멋사')           #갱신(수정)한 의사명
    docMaj=models.CharField(max_length=50, default='외과 전문의')     #갱신(수정)한 의사 전공
    Hospital=models.CharField(max_length=50, default='멋사 병원')      #갱신(수정)한 병원명


class Caution(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    info_id = models.ForeignKey(Medi_Info, on_delete=models.CASCADE)
    LEVEL_CHOICES = (
        ('SEVERE','Severe'),
        ('MODERATE','Moderate'),
        ('MILD','Mild')
    )
    cauLevel = models.CharField(max_length=10, choices=LEVEL_CHOICES)
    cauName = models.CharField(max_length=300)
    cauIngName = models.CharField(max_length=300, default='')
    cauIngType = models.CharField(max_length=300, default='')
    cauSymptom = models.CharField(max_length=300)

class Fam_History(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    info_id = models.ForeignKey(Medi_Info, on_delete=models.CASCADE)
    famRelation = models.CharField(max_length=100)
    famDiag = models.CharField(max_length=100)
    famBirth = models.DateField()
    famDeath = models.DateField(blank=True, null=True)
    famDReason = models.CharField(max_length=50, blank=True, null=True)

class Guardian(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    info_id = models.ForeignKey(Medi_Info, on_delete=models.CASCADE)
    guaName = models.CharField(max_length=20)
    guaRelation = models.CharField(max_length=100)
    guaPhone = models.CharField(max_length=13, default='010-1234-5678')

class Info_Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    originPost = models.ForeignKey(Medi_Info, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='replies')
    #user_type = models.ForeignKey(User.userType, on_delete=models.CASCADE)
    #user_name = models.ForeignKey(User.username, on_delete=models.CASCADE) 이름 어케 받을지 유저 모델과 함께 생각해보기
    
    comTitle = models.CharField(max_length=50)
    comContent = models.TextField()
    comDate = models.DateTimeField(auto_now_add=True)

    CATEGORY_CHOICES=(
        ('INFO','의료 정보'),
    )
    comCategory = models.CharField(max_length=4, choices=CATEGORY_CHOICES)

    def user_name(self):
        return self.user_id.userFullName

    def user_type(self):
        return self.user_id.userType