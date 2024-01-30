from django.shortcuts import render
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
from user.models import CustomUser, Grade
from competition.models import Competition, Attempt
from schoolbook.models import SchoolBook

@login_required
def Home(request):
    current_user = CustomUser.objects.get(id=request.user.id)
    users = CustomUser.objects.filter(grade=current_user.grade)
    grades = Grade.objects.all()
    competitions = Competition.objects.filter(terminated=False) 
    schoolbooks = SchoolBook.objects.filter(grade=request.user.grade.id)

    response_users = []

    for user in users:
        attempts_score = Attempt.objects.filter(user=user, finished=True).aggregate(Sum('score'))

        response_user = {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'grade': user.grade,
            'institution': user.institution,
        }

        response_user['score'] = 0 if attempts_score['score__sum'] is None else attempts_score['score__sum']
        response_users.append(response_user)

    response_users = sorted(response_users, key=lambda d: d['score'], reverse=True)
    index_of_current_user = next((index for (index, d) in enumerate(response_users) if d['id'] == current_user.id), None)

    for user in response_users:
        user['rank'] = next((index for (index, d) in enumerate(response_users) if d['id'] == user['id']), None) + 1

    attempts_of_user = Attempt.objects.filter(user=current_user.id, finished=True)
    accuracy = 0

    context={
        'user': {
            'id': current_user.id,
            'first_name': current_user.first_name,
            'last_name': current_user.last_name,
            'grade': current_user.grade,
            'institution': current_user.institution,
            'rank': index_of_current_user + 1,
            'is_authenticated': True,
            'points': response_users[index_of_current_user]['score'],
            'average_accuracy': 0
        },
        'top_users': response_users[:5],
        'grades': grades,
        'competitions': competitions,
        'schoolbooks': schoolbooks
    }
    
    return render(request, 'home/home.html', context)


def error_404_view(request, exception):
    return render(request, '404.html')