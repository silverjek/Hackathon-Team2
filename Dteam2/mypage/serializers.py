from rest_framework import serializers
from .models import *
from account.serializers import *

class myPageSerializer(serializers.ModelSerializer):
    class Meta:
        model=myPage
        fields=['userFullName' , 'userName', 'userAge', 'user_id']