from django.shortcuts import render, get_object_or_404
from rest_framework import views, status
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

class CommentListView(views.APIView):
    def get(self,request,first_pk,second_pk,format=None):
        user = get_object_or_404(User, pk=first_pk)
        surgery = get_object_or_404(Surgery, pk=second_pk)
        comments=Sur_Comment.objects.filter(originPost=surgery, user_id=user, parent=None)
        serializer= SurCommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
class AddCommentView(views.APIView):
    def post(self, request, format=None):
        data = request.data.copy()  
        data['user_id'] = request.user.id
        serializer = SurCommentSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UpadteCommentView(views.APIView):
     def get(self,request,pk,format=None):
        comments=get_object_or_404(Sur_Comment, pk=pk)
        serializer= SurCommentSerializer(comments)
        return Response(serializer.data)
     
     def put(self, request, pk, format=None):
        comment = get_object_or_404(Sur_Comment, pk=pk)
        
        #댓글 작성자와 접근자의 아이디가 같은지 확인
        if comment.user_id != request.user:
            return Response({'error': '이 댓글을 수정할 수 있는 권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        
        data = request.data.copy()
        data['user_id'] = request.user.id
        serializer = SurCommentSerializer(comment, data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteCommentView(views.APIView):
    def get(self,request,pk,format=None):
        comments=get_object_or_404(Sur_Comment, pk=pk)
        serializer= SurCommentSerializer(comments)
        return Response(serializer.data)
    
    def delete(self, request, pk, format=None):
        comment = get_object_or_404(Sur_Comment, pk=pk)
        
        #댓글 작성자와 접근자의 아이디가 같은지 확인
        if comment.user_id != request.user:
            return Response({'error': '이 댓글을 삭제할 수 있는 권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        
        comment.delete()
        return Response({"message": "댓글 삭제 성공"})
