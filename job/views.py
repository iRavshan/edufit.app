from django.shortcuts import render

def Jobs(request):
    return render(request, 'job/jobs.html')

