from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from rest_framework import views
from rest_framework.response import Response
from .models import *
from .serializers import *
from account.models import *
from account.serializers import *
from diagnosis.models import *
from diagnosis.serializers import *
from prescription.models import *
from prescription.serializers import *
from surgery.models import *
from surgery.serializers import *
from medicalinfo.models import *
from medicalinfo.serializers import *
# Create your views here.  
    
#내가 남긴 질문 페이지
class myPageView(views.APIView):
    def get(self,  request, pk, format=None):
        #mypage=myPage.objects.filter(user_id=pk)
        mypage=get_object_or_404(User, pk=pk)
        serializer=UserSerializer(mypage)
        return Response(serializer.data)    
    
#내가 남긴 질문 페이지
class myQAListView(views.APIView):
    def get(self, request, pk, format=None):
        myDiags = Diag_Comment.objects.filter(user_id=pk)

        myInfos = Info_Comment.objects.filter(user_id=pk)

        myPres = Pre_Comment.objects.filter(user_id=pk)

        mySurs = Sur_Comment.objects.filter(user_id=pk)

        myD_serializers = [DiagCommentSerializer(myDiag) for myDiag in myDiags]
        myI_serializers = [InfoCommentSerializer(myInfo) for myInfo in myInfos]
        myP_serializers = [PreCommentSerializer(myPre) for myPre in myPres]
        myS_serializers = [SurCommentSerializer(mySur) for mySur in mySurs]

        myD_data = [myD_serializer.data for myD_serializer in myD_serializers]
        myI_data = [myI_serializer.data for myI_serializer in myI_serializers]
        myP_data = [myP_serializer.data for myP_serializer in myP_serializers]
        myS_data = [myS_serializer.data for myS_serializer in myS_serializers]

        Qdata = {
            'myD': remove_replies_field(myD_data),
            'myI': remove_replies_field(myI_data),
            'myP': remove_replies_field(myP_data),
            'myS': remove_replies_field(myS_data),
        }
        return Response(Qdata)

def remove_replies_field(data_list):
    return [{key: value for key, value in data.items() if key != 'replies'} for data in data_list]