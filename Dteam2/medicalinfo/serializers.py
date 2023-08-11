from rest_framework import serializers
from .models import *

class CautionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caution
        fields = '__all__'

class FamHisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fam_History
        fields = '__all__'

class GuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardian
        fields = '__all__'

class MediInfoSerializer(serializers.ModelSerializer):
    caution = CautionSerializer(many=True, read_only=True)
    fam_history = FamHisSerializer(many=True, read_only=True)
    guardian = GuardianSerializer(many=True, read_only=True)
    class Meta:
        model = Medi_Info
        fields = ['user_id','patName','patSex','patBirth',
                  'patAddress','patSSN','patBlood','patRH',
                  'patHeight','patWeight','patPhone','updateDate',
                  'caution', 'fam_history', 'guardian']
