from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
# Model collect medical report from users
class MedicalReport(models.Model):
     user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_ids')
     # m=male and f=female and o=others
     gender = models.CharField(max_length=1)
     nationality = models.CharField(max_length=100)
     state = models.CharField(max_length=100)
     address = models.CharField(max_length=255)
     telephone = models.CharField(max_length=50)
     occupation = models.CharField(max_length=50)
     dob = models.DateField(blank=True, null=True)
     medical_condition = models.CharField(max_length=255)
     weight = models.IntegerField(blank=True, null=True)
     # m=married and s=single
     marital_status = models.CharField(max_length=1) 
     date_added = models.DateTimeField(default=datetime.now, blank=True, null=True)
     date_updated = models.DateTimeField(default=datetime.now, blank=True, null=True)

     def __str__(self):
        return self.user_id.email











# class MedicalCondition(models.Model):
#     doctor_id = models.ForeignKey(
#         User, on_delete=models.CASCADE)
#     medical_condition = models.CharField(max_length=150, blank=True)
#     date_added = models.DateTimeField(default=datetime.now, blank=True)
#     date_updated = models.DateTimeField(default=datetime.now, blank=True)
