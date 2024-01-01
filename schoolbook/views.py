from django.shortcuts import render

def Schoolbooks(request):
    return render(request, 'schoolbook/schoolbooks.html')