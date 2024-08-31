from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserSignUpForm, ChangeInfoForm



def sign_up(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password1']
            form.save()
            user = authenticate(request, phone_number=phone_number, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = UserSignUpForm()
    return render(request, 'auth/signup.html', {'form': form})



def sign_in(request):
    if request.method == "POST":
        username = request.POST.get('phone')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        messages.error(request, 'Foydalanuvchi nomi yoki parol xato')
        return redirect('login')
    return render(request, 'user/signin.html')



@login_required
def settings(request):

    context = {}

    if request.method == 'POST':
        form = ChangeInfoForm(request.POST, instance=request.user)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
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
def log_out(request):
    logout(request)
    return render(request, 'user/signin.html')