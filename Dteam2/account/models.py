from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20) 
    userType = models.BooleanField(default=True) #True-일반사용자 / False-의료인사용자