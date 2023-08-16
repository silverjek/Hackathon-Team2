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

class Diag_Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    originPost = models.ForeignKey(Diagnosis, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='replies')
    #user_type = models.ForeignKey(User.userType, on_delete=models.CASCADE)
    #user_name = models.ForeignKey(User.username, on_delete=models.CASCADE) 이름 어케 받을지 유저 모델과 함께 생각해보기
    
    comTitle = models.CharField(max_length=50)
    comContent = models.TextField()
    comDate = models.DateTimeField(auto_now_add=True)

    CATEGORY_CHOICES=(
        ('DIAG','진단 내역'),
    )
    comCategory = models.CharField(max_length=4, choices=CATEGORY_CHOICES)

    def user_name(self):
        return self.user_id.userFullName

    def user_type(self):
        return self.user_id.userType