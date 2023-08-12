from rest_framework import serializers
from .models import *

class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = '__all__'

class DiagCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diag_Comment
        fields = '__all__'

