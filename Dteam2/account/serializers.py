from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password','userType','userFullName','userSex','userAge','latestUpdate', 'photo']

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
    
    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("해당 아이디는 이미 존재합니다.")
        if len(value) > User._meta.get_field('username').max_length:
            raise serializers.ValidationError("아이디는 최대 20자 이내로 설정해야합니다.")
        return value
    def validate_password(self, value):
        min_password_length = 8
        max_password_length = 20

        if len(value) < min_password_length or len(value) > max_password_length:
            raise serializers.ValidationError("비밀번호는 최소 8자 최대 20자로 설정해야합니다.".format(min_password_length, max_password_length))
        return value

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
    
class LogoutSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    # 다른 필드들도 추가할 수 있음

    def logout(self, request):
        # 로그아웃 로직을 구현합니다.
        # 세션 무효화 등의 처리를 할 수 있습니다.
        # 이 예시에서는 아무 작업도 하지 않음
        pass
