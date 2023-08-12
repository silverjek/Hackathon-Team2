from django.shortcuts import render, get_object_or_404
from rest_framework import views, status
from rest_framework.response import Response
from .models import *
from .serializers import *
from account.models import *

# Create your views here.

#기본의료정보 등록
class MediInfo_Write(views.APIView):
    def post(self, request, format=None):
        medi_serializer=MediInfoSerializer(data=request.data)
        if medi_serializer.is_valid():
            medi_serializer.save()
            return Response(medi_serializer.data)
        return Response(medi_serializer.errors)

#알러지/부작용정보 등록     
class Caution_Write(views.APIView):
    def post(self, request, format=None):
        cau_serializer=CautionSerializer(data=request.data)
        if cau_serializer.is_valid():
            cau_serializer.save()
            return Response(cau_serializer.data)
        return Response(cau_serializer.errors)

#가족력정보 등록
class FamHis_Write(views.APIView):
    def post(self, request, format=None):
        fam_serializer=FamHisSerializer(data=request.data)
        if fam_serializer.is_valid():
            fam_serializer.save()
            return Response(fam_serializer.data)
        return Response(fam_serializer.errors)

#보호자정보 등록
class Guardian_Write(views.APIView):
    def post(self, request, format=None):
        gua_serializer=GuardianSerializer(data=request.data)
        if gua_serializer.is_valid():
            gua_serializer.save()
            return Response(gua_serializer.data)
        return Response(gua_serializer.errors)
    
#의료정보 상세조회
class MediInfoDetailView(views.APIView):
    def get(self, request, pk, format=None):
        mediinfo = get_object_or_404(Medi_Info, pk=pk)  # Medi_info 모델 pk
        cautions = Caution.objects.filter(info_id=pk)
        famhistories = Fam_History.objects.filter(info_id=pk)
        guardians = Guardian.objects.filter(info_id=pk)

        medi_serializer = MediInfoSerializer(mediinfo)
        cau_serializers = [CautionSerializer(caution) for caution in cautions]
        fam_serializers = [FamHisSerializer(famhistory) for famhistory in famhistories]
        gua_serializers = [GuardianSerializer(guardian) for guardian in guardians]

        combined_data = {
            'medi': medi_serializer.data,
            'cau': [cau_serializer.data for cau_serializer in cau_serializers],
            'fam': [fam_serializer.data for fam_serializer in fam_serializers],
            'gua': [gua_serializer.data for gua_serializer in gua_serializers]
        }

        return Response(combined_data)
    
class CommentListView(views.APIView):
    def get(self,request,first_pk,second_pk,format=None):
        user = get_object_or_404(User, pk=first_pk)
        mediinfo = get_object_or_404(Medi_Info, pk=second_pk)
        comments=Info_Comment.objects.filter(originPost=mediinfo, parent=None)
        serializer= InfoCommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
class AddCommentView(views.APIView):
    '''
    if User.userType == 'False': #유저가 의사인 경우, 환자의 원댓글 불러오기 pk 확인 필요
        def get(self,request,pk,format=None):
            comments=get_object_or_404(Info_Comment, pk=pk)
            serializer= InfoCommentSerializer(comments)
            return Response(serializer.data)
    '''
            
    def post(self,request,format=None):
        serializer = InfoCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class UpadteCommentView(views.APIView):
     '''
     if User.userType == 'False': #유저가 의사인 경우, 환자의 원댓글 불러오기 pk 확인 필요
        def get(self,request,pk,format=None):
            comments=get_object_or_404(Info_Comment, pk=pk)
            serializer= InfoCommentSerializer(comments)
            return Response(serializer.data)
    '''
            
     def get(self,request,pk,format=None):
        comments=get_object_or_404(Info_Comment, pk=pk)
        serializer= InfoCommentSerializer(comments)
        return Response(serializer.data)
     
     def put(self, request, pk, format=None):
        comment = get_object_or_404(Info_Comment, pk=pk)
        serializer = InfoCommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class DeleteCommentView(views.APIView):
    def get(self,request,pk,format=None):
        comments=get_object_or_404(Info_Comment, pk=pk)
        serializer= InfoCommentSerializer(comments)
        return Response(serializer.data)
    
    def delete(self, request, pk, format=None):
        comment = get_object_or_404(Info_Comment, pk=pk)
        comment.delete()
        return Response({"message":"댓글 삭제 성공"})
