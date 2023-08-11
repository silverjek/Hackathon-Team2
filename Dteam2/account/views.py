from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from .models import *
from .serializers import *
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
            return Response({'message':'로그인 성공', 'data':serializer.data})
        return Response({'message':'로그인 실패', 'error':serializer.errors})