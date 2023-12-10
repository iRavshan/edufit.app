from django.shortcuts import render
from user.models import CustomUser, Grade
from competition.models import Competition

def Home(request):
    user = CustomUser.objects.get(id=request.user.id)
    users = CustomUser.objects.filter(grade=user.grade)
    grades = Grade.objects.all()[:10]
    competitions = Competition.objects.filter(terminated=False)
    context={
        'user': user,
        'top_users': users,
        'grades': grades,
        'competitions': competitions
    }
    return render(request, 'home/authorizedHome.html', context)