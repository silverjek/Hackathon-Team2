from .views import *
from django.urls import path

app_name='medicalinfo'

urlpatterns=[
    path('write/', MediInfo_Write.as_view()),
    path('caution/write/', Caution_Write.as_view()),
    path('familyhistory/write/', FamHis_Write.as_view()),
    path('guardian/write/', Guardian_Write.as_view()),
    path('access/<int:pk>/', MediInfoDetailView.as_view()),
]