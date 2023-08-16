from rest_framework import serializers
from .models import *

class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = '__all__'

class DiagCommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    
    class Meta:
        model = Diag_Comment
        fields = ['id','user_id','user_name','user_type','originPost','parent',
                  'comTitle','comContent','comDate','comCategory',
                  'replies']

    def get_replies(self, instance):
        replies = instance.replies.all()  # Get all related replies
        serializer = self.__class__(replies, many=True)
        serializer.bind('', self)
        return serializer.data

