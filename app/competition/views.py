from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from user.models import Grade
from .models import Competition, Subject, Question, Option, Attempt


def Competitions(request):
    competitions = Competition.objects.all()
    context = {
        'competitions': competitions
    }
    return render(request, 'competition/competitions.html', context)


def Get(request, id):
    competition = Competition.objects.get(id=id)
    grades = competition.grades.all()
    subjects = competition.subjects.all()
    attempts = Attempt.objects.filter(competition=competition, finished=True).order_by('score')
    users = []

    for attempt in attempts:
        users.append({
            "first_name": attempt.user.first_name,
            "last_name": attempt.user.last_name,
            "institution": attempt.user.institution,
            "grade": attempt.user.grade,
            "score": attempt.score
        })

    context = {
        'competition': competition,
        'grades': grades,
        'subjects': subjects,
        'users': users
    }

    if request.user is not None:
        attempt = Attempt.objects.filter(user=request.user, competition=competition, finished=True)
        questions = Question.objects.filter(competition=competition).count()
        
        if attempt:
            context["user_score"] = {
                "rank": 0,
                "score": attempt[0].score,
                "accuracy": int((attempt[0].score / questions) * 100)
            }

    return render(request, 'competition/competition.html', context)


@login_required(login_url="/account/login")
def StartAttempt(request, competition_id, subject_name):
    competition = Competition.objects.get(id=competition_id)
    subject = Subject.objects.get(name=subject_name)
    questions = Question.objects.filter(competition=competition, subject=subject, grade=request.user.grade)
    response = []
    
    for question in questions:
        response.append({
            'id': question.id,
            'text': question.text,
            'options': Option.objects.filter(question=question)
        })

    context = {
        'competition': competition,
        'questions': response
    }

    attempt = Attempt.objects.filter(user=request.user, competition=competition)

    if not attempt:
        new_attempt = Attempt(user=request.user, competition=competition, subject=subject)
        new_attempt.save()
        context['attempt_id'] = new_attempt.id
    else:
        context['attempt_id'] = attempt[0].id

    return render(request, 'competition/attempt.html', context)


@login_required(login_url="/account/login")
def FinishAttempt(request, attempt_id):
    attempt = Attempt.objects.get(id=attempt_id)
    if attempt and request.method == 'POST':
        selectedOptions = request.POST.get('selectedOptions')
        selectedOptions = selectedOptions.split()
        attempt.finished_at = datetime.now()
        attempt.finished = True
        score = 0
        for selectedOption in selectedOptions:
            option = Option.objects.get(id=selectedOption)
            attempt.options.add(option)
            if(option.is_correct):
                score += 1
        attempt.score = score
        attempt.save()
    return Get(request, attempt.competition.id)

        
            

