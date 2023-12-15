from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from user.models import CustomUser, Grade
from competition.models import Competition

@login_required(login_url='/user/login')
def Home(request):
    user = CustomUser.objects.get(id=request.user.id)
    users = CustomUser.objects.filter(grade=user.grade)[:5]
    grades = Grade.objects.all()
    competitions = Competition.objects.filter(terminated=False) 
    context={
        'user': user,
        'top_users': users,
        'grades': grades,
        'competitions': competitions
    }
    return render(request, 'home/home.html', context)