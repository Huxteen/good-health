"""GoodHealth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from .import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('create-medical-report', views.create_medical_report, name='create_medical_report'),
    path('my-medical-report', views.my_medical_report, name='my_medical_report'),
    path('all-medical-report', views.all_medical_report, name='all_medical_report'),
    path('medical-statistics', views.medical_statistics, name='medical_statistics'),
    path('medical-api', views.medical_api, name='medical_api'),

] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
