from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, ChangeInfoForm

def Register(request):
    context = {}
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            middle_name = form.cleaned_data['middle_name']
            username = form.cleaned_data['username']
            institution = form.cleaned_data['institution']
            grade = form.cleaned_data['grade']
            password = form.cleaned_data['password1']
            try:
                instance = form.save(commit=False)
                instance.phone = username
                instance.save()
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
            except:
                context['form'] = form
                return render(request, 'user/register.html', context)
        else:
            context['form'] = form
            return render(request, 'user/register.html', context)
    context['form'] = UserRegistrationForm()
    return render(request, 'user/register.html', context)

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


@login_required
def Settings(request):

    context = {}

    if request.method == 'POST':
        form = ChangeInfoForm(request.POST, instance=request.user)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            middle_name = form.cleaned_data['middle_name']
            grade = form.cleaned_data['grade']
            institution = form.cleaned_data['institution']
        try:
            form.save()
            redirect('/')
        except:
            context['form'] = form
            return render(request, 'user/settings.html', context)
    
    context['form'] = ChangeInfoForm(instance=request.user)

    return render(request, 'user/settings.html', context)

@login_required
def Logout(request):
    logout(request)
    return render(request, 'user/login.html')