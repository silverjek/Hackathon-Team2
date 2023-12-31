from .views import *
from django.urls import path

app_name='account'

urlpatterns=[
    path('signup/', SignUpView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<int:pk>/doc_certification/', FileUploadView.as_view()),
]