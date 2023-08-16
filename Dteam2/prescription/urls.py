from .views import *
from django.urls import path

app_name='prescription'

urlpatterns=[
    path('write/', Prescription_Write.as_view()),
    path('medication/write/', Medication_Write.as_view()),
    path('access/<int:pk>/', PrescriptionListView.as_view()), 
    path('access/<int:first_pk>/<int:second_pk>', PrescriptionDetailView.as_view()),
    path('comment/<int:first_pk>/<int:second_pk>/', CommentListView.as_view()),
    path('comment/write/', AddCommentView.as_view()),
    path('comment/reply/write/<int:pk>', DOC_AddCommentView.as_view()),
    path('comment/reply/update/<int:pk>', DOC_UpdateCommentView.as_view()),
    path('comment/update/<int:pk>/', UpdateCommentView.as_view()),
    path('comment/delete/<int:pk>/', DeleteCommentView.as_view()),
]