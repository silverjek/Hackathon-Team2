from .views import *
from django.urls import path

app_name='medicalinfo'

urlpatterns=[
    path('write/', MediInfo_Write.as_view()),
    path('caution/write/', Caution_Write.as_view()),
    path('familyhistory/write/', FamHis_Write.as_view()),
    path('guardian/write/', Guardian_Write.as_view()),
    path('access/<int:pk>/', MediInfoDetailView.as_view()),
    path('comment/<int:first_pk>/<int:second_pk>/', CommentListView.as_view()),
    path('comment/write/', AddCommentView.as_view()),
    path('comment/update/<int:pk>/', UpdateCommentView.as_view()),
    path('comment/delete/<int:pk>/', DeleteCommentView.as_view()),
]