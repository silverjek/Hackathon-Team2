from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class SignUpView(views.APIView):
    def post(self, request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'회원가입 성공', 'data':serializer.data})
        return Response({'message':'회원가입 실패', 'error':serializer.errors})

class LoginView(views.APIView):
    def post(self, request):
        serializer=UserLoginSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            try:
                user = User.objects.get(username=username)
                if user.password == password:
                    return Response({'message': '로그인 성공', 'data': serializer.data})
                else:
                    return Response({'message': '로그인 실패', 'non_field_errors': ['잘못된 비밀번호입니다.']}, status=status.HTTP_401_UNAUTHORIZED)
            except User.DoesNotExist:
                return Response({'message': '로그인 실패', 'non_field_errors': ['존재하지 않는 아이디입니다.']}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'message': '로그인 실패', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

from rest_framework import views, status
from rest_framework.response import Response
from .serializers import LogoutSerializer

class LogoutView(views.APIView):
    def post(self, request, format=None):
        serializer = LogoutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.logout(request)
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





