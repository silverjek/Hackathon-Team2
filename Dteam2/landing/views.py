from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from rest_framework import views
from rest_framework.response import Response
from .models import *
from account.models import *
from account.serializers import *
from medicalinfo.models import *
from medicalinfo.serializers import *
from diagnosis.models import *
from diagnosis.serializers import *
from prescription.models import *
from prescription.serializers import *
from surgery.models import *
from surgery.serializers import *

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
        DNFTs=Diagnosis.objects.filter(info_id=pk)
        D_serializers = [DiagnosisSerializer(DNFT) for DNFT in DNFTs]
        D_data = [D_serializer.data for D_serializer in D_serializers]

        SNFTs=Surgery.objects.filter(info_id=pk)
        S_serializers = [SurgerySerializer(SNFT) for SNFT in SNFTs]
        S_data = [S_serializer.data for S_serializer in S_serializers]

        PNFTs=Prescription.objects.filter(info_id=pk)
        P_serializers = [PrescriptionSerializer(PNFT) for PNFT in PNFTs]
        P_data = [P_serializer.data for P_serializer in P_serializers]

        MNFTs=Medi_Info.objects.filter(pk=pk)
        M_serializers = [MediInfoSerializer(MNFT) for MNFT in MNFTs]
        M_data = [M_serializer.data for M_serializer in M_serializers]

        all_data = []
        for data in D_data + S_data + P_data + M_data:
            if 'updateDate' in data:
                all_data.append(data)

        all_data_sorted = sorted(all_data, key=lambda x: x['updateDate'], reverse=True)

        return Response(all_data_sorted)
        