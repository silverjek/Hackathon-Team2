from django.shortcuts import render, get_object_or_404
from rest_framework import views, status
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
    
class CommentListView(views.APIView):
    def get(self,request,first_pk,second_pk,format=None):
        user = get_object_or_404(User, pk=first_pk)
        diagnosis = get_object_or_404(Diagnosis, pk=second_pk)
        comments= Diag_Comment.objects.filter(originPost=diagnosis, user_id=user, parent=None)
        serializer= DiagCommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
class AddCommentView(views.APIView):
    def post(self, request, format=None):
        data = request.data.copy()  
        data['user_id'] = request.user.id
        serializer = DiagCommentSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UpadteCommentView(views.APIView):
     def get(self,request,pk,format=None):
        comments=get_object_or_404(Diag_Comment, pk=pk)
        serializer= DiagCommentSerializer(comments)
        return Response(serializer.data)
     
     def put(self, request, pk, format=None):
        comment = get_object_or_404(Diag_Comment, pk=pk)
        
        #댓글 작성자와 접근자의 아이디가 같은지 확인
        if comment.user_id != request.user:
            return Response({'error': '이 댓글을 수정할 수 있는 권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        
        data = request.data.copy()
        data['user_id'] = request.user.id
        serializer = DiagCommentSerializer(comment, data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteCommentView(views.APIView):
    def get(self,request,pk,format=None):
        comments=get_object_or_404(Diag_Comment, pk=pk)
        serializer= DiagCommentSerializer(comments)
        return Response(serializer.data)
    
    def delete(self, request, pk, format=None):
        comment = get_object_or_404(Diag_Comment, pk=pk)
        
        #댓글 작성자와 접근자의 아이디가 같은지 확인
        if comment.user_id != request.user:
            return Response({'error': '이 댓글을 삭제할 수 있는 권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        
        comment.delete()
        return Response({"message": "댓글 삭제 성공"})
