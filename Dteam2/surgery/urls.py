from .views import *
from django.urls import path

app_name='surgery'

urlpatterns=[
    path('write/', Surgery_Write.as_view()),
    path('access/<int:pk>/', SurgeryListView.as_view()), 
    path('access/<int:first_pk>/<int:second_pk>', SurgeryDetailView.as_view()),
]