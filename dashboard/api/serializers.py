from dashboard.models import MedicalReport
from rest_framework import serializers


class MedicalReportSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user_id.first_name')
    last_name = serializers.CharField(source='user_id.last_name')
    class Meta:
        model = MedicalReport
        fields = ('pk', 'user_id', 'nationality', 'gender',
                  'telephone', 'occupation', 'medical_condition', 'weight', 'date_added', 'first_name', 'last_name')
        read_only_fields = ('pk', 'user_id', 'nationality', 'gender',
                  'telephone', 'occupation', 'medical_condition', 'weight', 'date_added', 'first_name', 'last_name')
        
