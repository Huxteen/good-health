from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from collections import Counter
from dashboard.models import MedicalReport
from dashboard.forms import MedicalReportForm
from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib import auth
from django.shortcuts import get_object_or_404
from django.contrib import messages
from datetime import datetime
from django.utils import timezone

# Create your views here.


# Process and redirect login form data
@login_required(login_url="/accounts/login")
def dashboard(request):
    return redirect('medical_statistics')



# url to create medical report
@login_required(login_url="/accounts/login")
def create_medical_report(request):
    if request.method == 'POST':
        form = MedicalReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            user = int(request.user.id)
            report.user_id = User(pk=user)
            report.save()
            # successful form processing and redirect user
            messages.success(request, 'Your medical report has been created successfully')
            return redirect('my_medical_report')
        else:
            # form has error relay it to the user
            context = {'form': form}
            return render(request, 'dashboard/create_medical_report.html', context)
    else:
        return render(request, 'dashboard/create_medical_report.html')


# URL to get individual medical report of a logged-in user
@login_required(login_url="/accounts/login")
def my_medical_report(request):
    user = request.user.id
    my_medical_report = MedicalReport.objects.filter(user_id=user)
    context = {'my_medical_report':my_medical_report}
    return render(request, 'dashboard/my_medical_report.html', context)


# URL to get all medical report on the system
@login_required(login_url="/accounts/login")
def all_medical_report(request):
    # Check if the user is trying to filter a particular field
    if request.method == 'POST' and request.POST['search_element'] != 'none':
        search_element = (request.POST['search_element']).casefold()
        all_medical_report = MedicalReport.objects.filter(
            medical_condition=search_element)
        all_medical_conditions = MedicalReport.objects.values_list(
            'medical_condition')
        # select distnct value and count how many occurances
        all_statistics = Counter(all_medical_conditions)
        context = {'all_medical_report': all_medical_report, 'all_statistics': all_statistics}
        return render(request, 'dashboard/all_medical_report.html', context)

    else:
        # Load all medical report by default
        all_medical_report = MedicalReport.objects.all().order_by('-id')
        all_medical_conditions = MedicalReport.objects.values_list(
            'medical_condition')
        all_occupations = MedicalReport.objects.values_list(
            'occupation')
        # select distnct value and count how many occurances
        all_statistics = Counter(all_medical_conditions)
        occupations = Counter(all_occupations)
        context = {'all_medical_report': all_medical_report,
                   'all_statistics': all_statistics, 'occupations': occupations}
        return render(request, 'dashboard/all_medical_report.html', context)


@login_required(login_url="/accounts/login")
def medical_statistics(request):
    all_medical_conditions = MedicalReport.objects.values_list('medical_condition')
    # select only 11 medical condition with the highest number of occurances
    statistics = Counter(all_medical_conditions).most_common(11)
    # select all unique medical condition 
    all_statistics = Counter(all_medical_conditions)
    # Total number of report we have
    total_report = len(all_medical_conditions)

    # Total number of medical condition
    i = sum_distincts = 0
    while i < len(statistics):
        sum_distincts += statistics[i][1]
        i += 1
    other_statistics = total_report - sum_distincts
    context = {'all_statistics': all_statistics, 'other_statistics': other_statistics,
               'statistics': statistics, 'total_report': total_report}
    return render(request, 'dashboard/medical_statistics.html', context)
    

# not used
def medical_api(request):
    context = {
        "title": "The winning programming language",
        "description": "Programming is a game of consistency and strong determination to sollve challenging problems",
    }
    return JsonResponse(context)
