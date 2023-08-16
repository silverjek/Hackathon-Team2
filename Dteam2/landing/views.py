from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from rest_framework import views
from rest_framework.response import Response
from .models import *
from account.models import *
from account.serializers import *
from medicalinfo.models import *
from medicalinfo.serializers import *

# Create your views here.

#환자 랜딩 페이지
class PAT_NFTListView(views.APIView):
    def get(self, request, pk, format=None):
        nfts = User.objects.filter(pk=pk)
        serializer = UserSerializer(nfts, many=True)
        return Response(serializer.data)

#의사가 환자 NFT 접근 시 페이지        
class DOC_NFTDetailView(views.APIView):
    def get(self, request, pk, format=None):
        nftDetails=Medi_Info.objects.filter(pk=pk) #info_id=pk 아님
        serializer=MediInfoSerializer(nftDetails, many=True)
        return Response(serializer.data)

#갱신기록    
class NFTUpdateView(views.APIView):
    def get(self, request, pk, format=None):
        NFTs=Medi_Info.objects.filter(pk=pk)
        serializer=MediInfoSerializer(NFTs, many=True)
        return Response(serializer.data)