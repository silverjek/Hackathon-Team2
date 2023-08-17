from django.db import models
from account.models import *
from medicalinfo.models import *
from diagnosis.models import *

# Create your models here.

class Surgery(models.Model) :
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    info_id = models.ForeignKey(Medi_Info, on_delete=models.CASCADE)
    diag_id = models.ForeignKey(Diagnosis, on_delete=models.CASCADE)
    def diagDate(self):
        return self.diag_id.diagDate
    surChartNum = models.CharField(max_length=50)
    surRegi = models.CharField(max_length=50, default='')
    surCount = models.IntegerField(default=1)
    surWriter = models.CharField(max_length=20)
    surDate = models.DateField()
    surNum = models.IntegerField()
    surHospital = models.CharField(max_length=100)
    surField = models.CharField(max_length=300)
    surOper = models.CharField(max_length=20)
    surAssi = models.CharField(max_length=20)
    surAnesDoc = models.CharField(max_length=20)
    surName = models.CharField(max_length=100)
    surCode = models.CharField(max_length=50)
    surPreDiag = models.CharField(max_length=100)
    surPostDiag = models.CharField(max_length=100)
    surAnes = models.CharField(max_length=100)
    surEvent = models.BooleanField(default=False) #False-무 / True-유
    surRemoval = models.BooleanField(default=False) #False-무 / True-유
    surBloodTrans = models.BooleanField(default=False) #False-무 / True-유
    surPre = models.TextField(null=False, blank=False, default='')
    surDur = models.TextField(null=False, blank=False, default='')
    surPost = models.TextField(null=False, blank=False, default='')
    surTube = models.BooleanField(default=False) #False-무 / True-유
    updateDate = models.DateTimeField(auto_now_add=True)
    surDocMaj=models.CharField(max_length=50, default="외과 전문의")
    
    

class Sur_Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    originPost = models.ForeignKey(Surgery, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='replies')
    #user_type = models.ForeignKey(User.userType, on_delete=models.CASCADE)
    #user_name = models.ForeignKey(User.username, on_delete=models.CASCADE) 이름 어케 받을지 유저 모델과 함께 생각해보기
    
    comTitle = models.CharField(max_length=50)
    comContent = models.TextField()
    comDate = models.DateTimeField(auto_now_add=True)

    CATEGORY_CHOICES=(
        ('SUR','수술 내역'),
    )
    comCategory = models.CharField(max_length=4, choices=CATEGORY_CHOICES)

    def user_name(self):
        return self.user_id.userFullName

    def user_type(self):
        return self.user_id.userType