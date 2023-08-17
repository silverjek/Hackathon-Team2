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
        fields = ['id','user_id','patName','patSex','patBirth','patAge'
                  'patAddress','patSSN','patBlood','patRH',
                  'patHeight','patWeight','patPhone','updateDate',
                  'caution', 'fam_history', 'guardian', 'doc', 'docMaj', 'Hospital']
        
class InfoCommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    
    class Meta:
        model = Info_Comment
        fields = ['id','user_id','user_name','user_type','originPost','parent',
                  'comTitle','comContent','comDate','comCategory',
                  'replies']
        
    def get_replies(self, instance):
        replies = instance.replies.all()  # Get all related replies
        serializer = self.__class__(replies, many=True)
        serializer.bind('', self)
        return serializer.data
