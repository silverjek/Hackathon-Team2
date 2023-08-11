from django.shortcuts import render, get_object_or_404
from rest_framework import views
from rest_framework.response import Response
from .models import *
from .serializers import *
from medicalinfo.serializers import *

# Create your views here.

#진단정보 등록
class Diagnosis_Write(views.APIView):
    def post(self, request, format=None):
        diag_serializer=DiagnosisSerializer(data=request.data)
        if diag_serializer.is_valid():
            diag_serializer.save()
            return Response(diag_serializer.data)
        return Response(diag_serializer.errors)
    
#진단 리스트
class DiagnosisListView(views.APIView):
    def get(self, request, pk, format=None):
        diags = Diagnosis.objects.filter(info_id=pk)
        serializer = DiagnosisSerializer(diags, many=True) #필드 제한 필요
        return Response(serializer.data)
    
#진단 상세조회
class DiagnosisDetailView(views.APIView):
    def get(self, request, first_pk, second_pk, format=None):
        mediinfo = get_object_or_404(Medi_Info, pk=first_pk)  # Medi_info 모델 pk
        diagnosiss = get_object_or_404(Diagnosis, id=second_pk)

        medi_serializer = MediInfoSerializer(mediinfo)
        #diag_serializers = [DiagnosisSerializer(diagnosis,many=True) for diagnosis in diagnosiss]
        diag_serializers = DiagnosisSerializer(diagnosiss)

        combined_data = {
            'medi': medi_serializer.data,
            #'diag': [diag_serializer.data for diag_serializer in diag_serializers]
            'diag': diag_serializers.data
        }

        return Response(combined_data)