from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from rest_framework import views
from rest_framework.response import Response
from .models import *
from .serializers import *
from account.models import *
from account.serializers import *
# Create your views here.

class myPageView(views.APIView):
    def get(self,  request, pk, format=None):
        #mypage=myPage.objects.filter(user_id=pk)
        mypage=get_object_or_404(User, pk=pk)
        serializer=UserSerializer(mypage)
        return Response(serializer.data)    