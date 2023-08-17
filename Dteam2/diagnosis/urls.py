from .views import *
from django.urls import path

app_name='diagnosis'

urlpatterns=[
    path('write/', Diagnosis_Write.as_view()),
    path('access/<int:pk>/', DiagnosisListView.as_view()), #doctor와 patient의 권한 구분 없이 함수를 쓴다면 url 분리할 필요 X
    path('access/<int:first_pk>/<int:second_pk>', DiagnosisDetailView.as_view()),
    path('comment/<int:first_pk>/<int:second_pk>/', CommentListView.as_view()),
    path('comment/write/<int:pk>/', AddCommentView.as_view()),
    path('comment/reply/write/<int:pk>/', DOC_AddCommentView.as_view()),
    path('comment/reply/update/<int:pk>/', DOC_UpdateCommentView.as_view()),
    path('comment/update/<int:pk>/', UpdateCommentView.as_view()),
    path('comment/delete/<int:pk>/', DeleteCommentView.as_view()),
]