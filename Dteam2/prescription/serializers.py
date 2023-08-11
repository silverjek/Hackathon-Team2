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
