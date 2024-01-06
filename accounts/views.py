from django.shortcuts import render ,HttpResponse, redirect
from .forms import *
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib import messages
from django.urls import reverse_lazy
# Create your views here.

def user_login(request):
    if request.user.is_authenticated:
        return redirect('core:dashboard')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'], password=cd['password'])
            if user != None:
                if user.is_active:
                    login(request, user)
                    messages.success(request,f'Welcome {user.username} 😃',extra_tags='success')
                    next_page = request.GET.get('next', 'core:home')
                    return redirect(next_page)
                else:
                    form.add_error('username', 'User is not active')
            else:
                form.add_error('username', 'Wrong Username/Password')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form':form})
@login_required
def user_logout(request):
        username = request.user.username
        logout(request)
        messages.success(request,f'{username} successfully logged out!', 'success')
        return redirect('core:home')

def sign_up(request):
    if request.user.is_authenticated:
        return redirect('core:dashboard')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request,f'Welcome To SoundScapes {user.username}😃',extra_tags='success')
            return redirect('core:dashboard')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html',{'form': form})
