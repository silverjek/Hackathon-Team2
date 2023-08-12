from rest_framework import serializers
from .models import *
from diagnosis.serializers import *
from medicalinfo.serializers import *

class SurgerySerializer(serializers.ModelSerializer):
    diagnosis = DiagnosisSerializer(many=True, read_only=True)
    mediinfo = MediInfoSerializer(many=True, read_only=True)
    class Meta:
        model = Surgery
        fields = ['user_id','info_id','diag_id','surChartNum',
                  'surWriter','surDate','surNum','surHospital',
                  'surField','surOper','surAssi','surAnesDoc',
                  'surName','surCode','surPreDiag','surPostDiag',
                  'surAnes','surEvent','surRemoval','surBloodTrans',
                  'surPre','surDur','surPost','surTube',
                  'diagnosis','mediinfo']
        
class SurCommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    class Meta:
        model = Sur_Comment
        fields = ['id','user_id','originPost','parent',
                  'comTitle','comContent','comDate','comCategory',
                  'replies']

    def get_replies(self, instance):
        replies = instance.replies.all()  # Get all related replies
        serializer = self.__class__(replies, many=True)
        serializer.bind('', self)
        return serializer.data
