from django.shortcuts import render, get_object_or_404
from rest_framework import views
from rest_framework.response import Response
from .models import *
from .serializers import *
from medicalinfo.serializers import *

# Create your views here.

#수술 정보등록    
class Surgery_Write(views.APIView):
    def post(self, request, format=None):
        sur_serializer=SurgerySerializer(data=request.data)
        if sur_serializer.is_valid():
            sur_serializer.save()
            return Response(sur_serializer.data)
        return Response(sur_serializer.errors)
    
#수술 리스트
class SurgeryListView(views.APIView):
    def get(self, request, pk, format=None):
        surs = Surgery.objects.filter(info_id=pk)
        serializer = SurgerySerializer(surs, many=True) #필드 제한 필요
        return Response(serializer.data)
    
#수술 상세조회
class SurgeryDetailView(views.APIView):
    def get(self, request, first_pk, second_pk, format=None):
        mediinfo = get_object_or_404(Medi_Info, pk=first_pk)  # Medi_info 모델 pk
        surgerys = get_object_or_404(Surgery, pk=second_pk)
        diagnosiss = [surgerys.diag_id] ##여기가 문제!!!

        medi_serializer = MediInfoSerializer(mediinfo)
        sur_serializers = SurgerySerializer(surgerys)
        diag_serializers = [DiagnosisSerializer(diagnosis) for diagnosis in diagnosiss]
        
        
        combined_data = {
            'medi': medi_serializer.data,
            'sur': sur_serializers.data,
            'diag': [diag_serializer.data for diag_serializer in diag_serializers]
        }

        return Response(combined_data)
