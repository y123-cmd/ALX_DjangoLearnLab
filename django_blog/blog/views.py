from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# User Registration View
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# User Login View
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# User Logout View
def user_logout(request):
    logout(request)
    return redirect('login')

# Profile Management View
@login_required
def profile(request):
    if request.method == 'POST':
        new_email = request.POST.get('email')
        if new_email:
            request.user.email = new_email
            request.user.save()
            messages.success(request, 'Email updated successfully')
            return redirect('profile')
    return render(request, 'profile.html')

