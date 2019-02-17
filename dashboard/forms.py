from django.utils import timezone
from datetime import datetime
from django import forms
from django.forms import ModelForm
from . import models
from django.contrib.auth import get_user_model
User = get_user_model()



class MedicalReportForm(ModelForm):
    gender = forms.CharField(max_length=1, required=True)
    nationality = forms.CharField(max_length=100, required=True)
    state = forms.CharField(max_length=100, required=True)
    address = forms.CharField(max_length=255, required=True)
    telephone = forms.CharField(max_length=50, required=True)
    occupation = forms.CharField(max_length=50, required=True)
    medical_condition = forms.CharField(max_length=255, required=True)
    marital_status = forms.CharField(max_length=1, required=True)    

    class Meta:
        model = models.MedicalReport
        fields = (
            'gender',
            'nationality',
            'state',
            'address',
            'telephone',
            'occupation',
            'dob',
            'medical_condition',
            'weight',
            'marital_status',
        )

    def save(self, commit=True):
        report = super(MedicalReportForm, self).save(commit=False)
        report.gender = (self.cleaned_data['gender']).casefold()
        report.nationality = (self.cleaned_data['nationality']).casefold()
        report.state = self.cleaned_data['state']
        report.address = self.cleaned_data['address']
        report.telephone = self.cleaned_data['telephone']
        report.occupation = (self.cleaned_data['occupation']).casefold()
        report.dob = self.cleaned_data['dob']
        report.medical_condition = (self.cleaned_data['medical_condition']).casefold()
        report.weight = self.cleaned_data['weight']
        report.marital_status = (self.cleaned_data['marital_status']).casefold()
        report.date_added = timezone.datetime.now()
        report.date_updated = timezone.datetime.now()

        if commit:
            report.save()

        return report


# class SearchForm(ModelForm):
#     medical_condition = forms.CharField(max_length=255, required=True)

#     class Meta:
#         model = models.MedicalReport
#         fields = (
#             'medical_condition',
#         )
