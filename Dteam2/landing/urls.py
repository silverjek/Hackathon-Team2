from .views import *
from django.urls import path

app_name='landing'

urlpatterns=[
    path('patient/main/<int:pk>/', PAT_NFTListView.as_view()),
    path('doctor/access/<int:pk>/', DOC_NFTDetailView.as_view()),
    path('access/<int:pk>/update/', NFTUpdateView.as_view()),
]