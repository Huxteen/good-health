from .serializers import MedicalReportSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from dashboard.models import MedicalReport
from django_filters import FilterSet
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend


# class based custom filters
class MedicalReportFilter(FilterSet):
    medical_condition = filters.CharFilter('medical_condition')
    nationality = filters.CharFilter('nationality')
    occupation = filters.CharFilter('occupation')
    gender = filters.CharFilter('gender')

    class Meta:
        model = MedicalReport
        # fields you can filter from
        fields = ('medical_condition', 'occupation', 'gender', 'nationality')


# Generic ListAPIView To filter with a custom class
class MedicalReportAPIView(generics.ListAPIView):
    queryset = MedicalReport.objects.all()
    serializer_class = MedicalReportSerializer
    permission_classes = (IsAdminUser,)
    filter_backends = (DjangoFilterBackend, )
    filter_class = MedicalReportFilter
    


    
# class MedicalReportAPIView(generics.ListAPIView):
#     lookup_field = "pk"
#     queryset = MedicalReport.objects.all()
#     serializer_class = MedicalReportSerializer
#     permission_classes = (IsAdminUser,)
#     filter_class = MedicalReportFilter

    
