from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20) 
    userType = models.BooleanField(default=True) #True-일반사용자 / False-의료인사용자
    userFullName = models.CharField(max_length=20)
    SEX_CHOICES = (
        ('MALE','Male'),
        ('FEMALE','Female')
    )
    userSex = models.CharField(max_length=6, choices=SEX_CHOICES)
    userAge = models.IntegerField(default=0)
    latestUpdate = models.DateTimeField(blank=True, null=True)
    photo=models.ImageField(blank=True, null=True, upload_to="uplaod")
