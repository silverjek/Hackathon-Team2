from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate
from rest_framework import views
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import AllowAny

# Create your views here.

class SignUpView(views.APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'회원가입 성공', 'data':serializer.data})
        return Response({'message':'회원가입 실패', 'error':serializer.errors})

#로그인 함수
class LoginView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        user = get_object_or_404(User, id=request.user.id)
        serializer = UserLoginSerializer(user)
        return Response({'message': '현재 로그인된 유저 정보 조회 성공', 'data': serializer.data}, status=HTTP_200_OK)

    def post(self, request):
        user = authenticate(
            username=request.data.get("username"), password=request.data.get("password")
        )
        if user is not None:
            serializer = UserLoginSerializer(user)
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    'message': '로그인 성공',
                    "user": serializer.data,
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            res.set_cookie("access", access_token, httponly=True)
            res.set_cookie("refresh", refresh_token, httponly=True)
            return res
        else:
            return Response({'message': '로그인 실패'}, status=status.HTTP_400_BAD_REQUEST)
    

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

class FileUploadView(views.APIView):
    def post(self, request, pk, format=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'message': '해당 사용자가 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)

        if not user.userType:
            return Response({'message': '의료인 사용자만 파일을 업로드할 수 있습니다.'}, status=status.HTTP_403_FORBIDDEN)

        photo = request.FILES.get('photo')

        if photo:
            user.photo = photo
            user.save()
            return Response({'message': '사진이 성공적으로 저장되었습니다.'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': '사진 파일을 업로드해야 합니다.'}, status=status.HTTP_400_BAD_REQUEST)



