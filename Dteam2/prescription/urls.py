from .views import *
from django.urls import path

app_name='prescription'

urlpatterns=[
    path('write/', Prescription_Write.as_view()),
    path('medication/write/', Medication_Write.as_view()),
    path('access/<int:pk>/', PrescriptionListView.as_view()), 
    path('access/<int:first_pk>/<int:second_pk>', PrescriptionDetailView.as_view()),
]