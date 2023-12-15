from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from user.models import CustomUser, Grade

def Rating(request):
    user = CustomUser.objects.get(id=request.user.id)
    users = CustomUser.objects.filter(grade=user.grade)    
    grades = Grade.objects.all()

    paginator = Paginator(users, 15)
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