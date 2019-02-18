from django.contrib.auth.decorators import login_required
from accounts.forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.contrib.auth import get_user_model
User = get_user_model()
from django.shortcuts import get_object_or_404
from django.contrib import messages




# Create your views here.


# Process and redirect login form data
def login(request):
    # if you are logged-in you shouldnt be able to visit the login URL
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            # Authenticate users input and match it to our database record and return a response
            user = auth.authenticate(
                email=(request.POST['email']).casefold(),
                password=request.POST['password']
            )
            # if find match, take the user to our dashboard page
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
            # if we couldnt find a match take them back to the login page with the error 
            else:
                messages.error(
                    request, 'Email or password do not match our record')
                return render(request, 'accounts/login.html')
        else:
            return render(request, 'accounts/login.html')


def signup(request):
    # if you are logged-in you shouldnt be able to visit the signup URL
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid(): 
                # form is a valid response then save the data               
                user = User.objects.create_user(
                    email=(form.cleaned_data['email']).casefold(),
                    password=form.cleaned_data['password1'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    is_staff=int(request.POST['is_staff']),
                )                
                auth.login(request, user)
                return redirect('dashboard')
                # messages.success(request, 'Account creation was successful. Please, login to dashboard')
                # return redirect('login')
            else:
                # Form has error relay the error to the user
                context = {'form':form}
                return render(request, 'accounts/signup.html', context)
        else:
            return render(request, 'accounts/signup.html')


# The logout function, kills all active session
@login_required(login_url="/accounts/login")
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')
