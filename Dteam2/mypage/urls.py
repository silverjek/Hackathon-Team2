from .views import *
from django.urls import path

app_name='mypage'

urlpatterns=[
    path('<int:pk>/', myPageView.as_view()),
]