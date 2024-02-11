from django.shortcuts import render
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from user.models import CustomUser, Grade
from competition.models import Attempt


def Rating(request):
    if request.user.is_authenticated:
        user = CustomUser.objects.get(id=request.user.id)
        users = CustomUser.objects.filter(grade=user.grade)    
    else:
        users = CustomUser.objects.filter(grade=5)    
    grades = Grade.objects.all()

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

    for user in response_users:
        user['rank'] = next((index for (index, d) in enumerate(response_users) if d['id'] == user['id']), None) + 1

    paginator = Paginator(response_users, 15)
    page_number = request.GET.get('page', 1)

    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    page_obj = paginator.get_page(page_number)

    context = {
        "grades": grades,
        "page_obj": page_obj
    }

    return render(request, 'rating/rating.html', context)