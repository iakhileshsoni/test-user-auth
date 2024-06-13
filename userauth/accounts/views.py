from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, PasswordResetView
from .forms import UserRegistrationForm, UserLoginForm, UserPasswordResetForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import CustomUser


# Register View
def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, "Email is already registered")
                return redirect('login')
            else:
                user = form.save()
                login(request, user)
                return redirect('home')
        
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form':form})


# Login View
def LoginView(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid credentials')
                return redirect('login')
            
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form':form})


# Home View
def home(request):
    return render(request, 'accounts/home.html')


# Password Reset View
def password_reset(request):
    if request.method == "POST":
        form = UserPasswordResetForm(request.POST)
        if form.is_valid():
            form.save(request=request, use_https=request.is_secure(), email_template_name='accounts/password_reset.html',)
            messages.success(request, 'Password reset linkhas been sent to your email')
            return redirect('login')
        
    else:
        form = UserPasswordResetForm()
    return render(request, 'accounts/password_reset.html')
