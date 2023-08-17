from django.shortcuts import render, get_object_or_404
from rest_framework import views, status
from rest_framework.response import Response
from .models import * 
from .serializers import *
from medicalinfo.serializers import *

# Create your views here.

#처방 정보등록    
class Prescription_Write(views.APIView):
    def post(self, request, format=None):
        pre_serializer=PrescriptionSerializer(data=request.data)
        if pre_serializer.is_valid():
            pre_serializer.save()
            return Response(pre_serializer.data)
        return Response(pre_serializer.errors)
    
#약 정보등록    
class Medication_Write(views.APIView):
    def post(self, request, format=None):
        med_serializer=MedicationSerializer(data=request.data)
        if med_serializer.is_valid():
            med_serializer.save()
            return Response(med_serializer.data)
        return Response(med_serializer.errors)
    
#약물처방 리스트
class PrescriptionListView(views.APIView):
    def get(self, request, pk, format=None):
        pres = Prescription.objects.filter(info_id=pk)
        serializer = PrescriptionSerializer(pres, many=True) #필드 제한 필요
        return Response(serializer.data)
    
#약물처방 상세조회
class PrescriptionDetailView(views.APIView):
    def get(self, request, first_pk, second_pk, format=None):
        mediinfo = get_object_or_404(Medi_Info, pk=first_pk)  # Medi_info 모델 pk
        #prescriptions = Caution.objects.filter(pk=second_pk)
        prescriptions = get_object_or_404(Prescription, pk=second_pk)
        medications = Medication.objects.filter(pre_id=second_pk) #얘 pk 이렇게 받는게 맞나..?

        medi_serializer = MediInfoSerializer(mediinfo)
        pre_serializers = PrescriptionSerializer(prescriptions)
        med_serializers = [MedicationSerializer(medication) for medication in medications]
        
        combined_data = {
            'medi': medi_serializer.data,
            'pre': pre_serializers.data,
            'med': [med_serializer.data for med_serializer in med_serializers]
        }

        return Response(combined_data)
    
class CommentListView(views.APIView):
    def get(self,request,first_pk,second_pk,format=None):
        user = get_object_or_404(User, pk=first_pk)
        prescription = get_object_or_404(Prescription, pk=second_pk)
        comments=Pre_Comment.objects.filter(originPost=prescription, user_id=user, parent=None)
        serializer= PreCommentSerializer(comments, many=True)
        return Response(serializer.data)

    
class AddCommentView(views.APIView):
    def post(self, request, pk, format=None):
        data = request.data.copy()  
        data['user_id'] = request.user.id
        data['originPost'] = pk
        serializer = PreCommentSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateCommentView(views.APIView):
    def get(self,request,pk,format=None):
        comments=get_object_or_404(Pre_Comment, pk=pk)
        serializer= PreCommentSerializer(comments)
        return Response(serializer.data)
     
    def put(self, request, pk, format=None):
        comment = get_object_or_404(Pre_Comment, pk=pk)
        
        #댓글 작성자와 접근자의 아이디가 같은지 확인
        if comment.user_id != request.user:
            return Response({'error': '이 댓글을 수정할 수 있는 권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        
        data = request.data.copy()
        data['user_id'] = request.user.id
        serializer = PreCommentSerializer(comment, data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteCommentView(views.APIView):
    def get(self,request,pk,format=None):
        comments=get_object_or_404(Pre_Comment, pk=pk)
        serializer= PreCommentSerializer(comments)
        return Response(serializer.data)
    
    def delete(self, request, pk, format=None):
        comment = get_object_or_404(Pre_Comment, pk=pk)
        
        #댓글 작성자와 접근자의 아이디가 같은지 확인
        if comment.user_id != request.user:
            return Response({'error': '이 댓글을 삭제할 수 있는 권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        
        comment.delete()
        return Response({"message": "댓글 삭제 성공"})

class DOC_AddCommentView(views.APIView): 
    def post(self, request, pk, format=None):
        data = request.data.copy()  
        data['user_id'] = request.user.id
        data['parent'] = pk
        serializer = PreCommentSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,pk,format=None): #원본 댓글 불러오기
        parent=get_object_or_404(Pre_Comment, pk=pk)
        serializer= PreCommentSerializer(parent)
        return Response(serializer.data)

class DOC_UpdateCommentView(views.APIView):
    def get(self,request,pk,format=None): #본인이 작성한 내용 불러오기
        comments=get_object_or_404(Pre_Comment, pk=pk) #수정할 대댓글
        serializer= PreCommentSerializer(comments)

        parent_comment = comments.parent
        combined_data = {
            'parent': PreCommentSerializer(parent_comment).data,
            'comment': serializer.data
        }
        
        return Response(combined_data)
    
    def put(self, request, pk, format=None):
        comment = get_object_or_404(Pre_Comment, pk=pk)
        
        #댓글 작성자와 접근자의 아이디가 같은지 확인
        if comment.user_id != request.user:
            return Response({'error': '이 댓글을 수정할 수 있는 권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        
        data = request.data.copy()
        data['user_id'] = request.user.id
        serializer = PreCommentSerializer(comment, data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)