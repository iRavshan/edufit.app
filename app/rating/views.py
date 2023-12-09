from django.shortcuts import render
from user.models import CustomUser, Grade

def Rating(request):
    user = CustomUser.objects.get(id=request.user.id)
    users = CustomUser.objects.filter(grade=user.grade)    
    grades = Grade.objects.all()
    context = {
        "users": users,
        "grades": grades
    }
    return render(request, 'rating/rating.html', context)