from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def Register(request):
    return render(request, 'user/register.html')

def Login(request):
    if request.method == "POST":
        username = request.POST.get('phone')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        messages.error(request, 'Foydalanuvchi nomi yoki parol xato')
        return redirect('login')
    return render(request, 'user/login.html')

@login_required(login_url="/account/login")
def Logout(request):
    logout(request)
    return render(request, 'user/login.html')