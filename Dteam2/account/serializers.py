from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password','userType','userFullName','userSex','userAge']

    def create(self, validated_data):
        user=User.objects.create(
            userType=validated_data['userType'],
            username=validated_data['username'],
            userFullName=validated_data['userFullName'],
            userSex=validated_data['userSex'],
            userAge=validated_data['userAge']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

class UserLoginSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=20)
    password=serializers.CharField(max_length=20, write_only=True)
    userType=serializers.BooleanField(default=True)

    def validate(self, data):
        username=data.get("username", None)
        password=data.get("password", None)

        if User.objects.filter(username=username).exists():
            user=User.objects.get(username=username)

            if not user.check_password(password):
                raise serializers.ValidationError("Incorrect password")
            else:
                return user
            
        raise serializers.ValidationError("User does not exist")
