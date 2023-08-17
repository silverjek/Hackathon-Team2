from django.db import models
from account.models import *
from diagnosis.models import *
from medicalinfo.models import *
from prescription.models import *
from surgery.models import *

# Create your models here.

class myPage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def user_id(self):
        return self.user.pk
    
    def userName(self):
        return self.user.username
    
    def userAge(self):
        return self.user.userAge
    
    def userFullName(self):
        return self.user.userFullName
    