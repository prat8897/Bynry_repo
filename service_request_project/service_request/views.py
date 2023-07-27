from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required 
from .forms import ServiceRequestForm
from .models import ServiceRequest
from .forms import UserRegistrationForm

@login_required
def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            if request.user.is_authenticated:
                service_request.user = request.user  # Set the 'user' field to the currently logged-in user
            service_request.save()
            return redirect('service_request:dashboard')
    else:
        form = ServiceRequestForm()

    return render(request, 'submit_service_request.html', {'form': form})

def track_service_request(request):
    service_requests = ServiceRequest.objects.all()
    return render(request, 'track_service_request.html', {'service_requests': service_requests})

def signup_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('service_request:dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('service_request:dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('service_request:login')

@login_required
def dashboard_view(request):
    if request.user.is_authenticated:
        service_requests = ServiceRequest.objects.filter(user=request.user)
        has_service_requests = service_requests.exists()

        return render(request, 'dashboard.html', {'service_requests': service_requests, 'has_service_requests': has_service_requests})
    else:
        return render(request, 'dashboard.html')
    
@login_required
def account_info_view(request):
    return render(request, 'account_info.html')