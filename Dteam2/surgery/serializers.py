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
