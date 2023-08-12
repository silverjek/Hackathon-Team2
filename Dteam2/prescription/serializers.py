from rest_framework import serializers
from .models import *

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'

class PrescriptionSerializer(serializers.ModelSerializer):
    medication = MedicationSerializer(many=True, read_only=True)
    class Meta:
        model = Prescription
        fields = ['user_id','info_id','diag_id','prePharm',
                  'preAddress','preDate','preChem','updateDate',
                  'medication']

class PreCommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    class Meta:
        model = Pre_Comment
        fields = ['id','user_id','originPost','parent',
                  'comTitle','comContent','comDate','comCategory',
                  'replies']

    def get_replies(self, instance):
        replies = instance.replies.all()  # Get all related replies
        serializer = self.__class__(replies, many=True)
        serializer.bind('', self)
        return serializer.data