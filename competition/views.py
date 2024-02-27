import random
import openpyxl
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from datetime import datetime, timedelta
from user.models import Grade
from schoolbook.models import Subject
from .models import Competition, Question, Option, Attempt
from user.models import CustomUser


def Competitions(request):
    competitions = Competition.objects.all()
    context = {
        'competitions': competitions
    }
    return render(request, 'competition/competitions.html', context)


def Get(request, competition_slug):
    competition = Competition.objects.get(slug=competition_slug)
    grades = competition.grades.all()
    subjects = competition.subjects.all()
    attempts = Attempt.objects.filter(competition=competition, finished=True).order_by('score')
    users = []

    for attempt in attempts:
        users.append({
            "id": attempt.user.id,
            "first_name": attempt.user.first_name,
            "last_name": attempt.user.last_name,
            "institution": attempt.user.institution,
            "grade": attempt.user.grade,
            "score": attempt.score,
            "time": attempt.finished_at - attempt.started_at,
            "formatted_time": chop_microseconds(attempt.finished_at - attempt.started_at)
        })

    users = sorted(users, key=lambda d: (d['score'], -d['time']), reverse=True)

    context = {
        'competition': competition,
        'grades': grades,
        'subjects': subjects,
        'users': users
    }

    if request.user.is_authenticated:
        attempt = Attempt.objects.filter(user=request.user, competition=competition, finished=True)
        questions = Question.objects.filter(competition=competition).count()
        
        if attempt:
            context["user_score"] = {
                "rank": next((index for (index, d) in enumerate(users) if d["id"] == request.user.id), None) + 1,
                "score": attempt[0].score,
                "accuracy": int((attempt[0].score / questions) * 100)
            }

    return render(request, 'competition/competition.html', context)


@login_required
def StartAttempt(request, competition_slug, subject_slug):
    competition = Competition.objects.get(slug=competition_slug)
    subject = Subject.objects.get(slug=subject_slug)
    questions = Question.objects.filter(competition=competition, subject=subject, grade=request.user.grade)
    response = []
    
    for question in questions:
        options = list(Option.objects.filter(question=question))
        random.shuffle(options)

        response.append({
            'id': question.id,
            'text': question.text,
            'options': options
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


@login_required
@require_http_methods('POST')
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
            if(option.is_correct == True):
                score += 1
        attempt.score = score
        attempt.save()
    competition = Competition.objects.get(id=attempt.competition.id)
    return Get(request, competition.slug)


@login_required
def GetAttempt(request, competition_slug):
    competition = Competition.objects.get(slug=competition_slug)
    attempt = Attempt.objects.get(user=request.user, competition=competition.id)
    selectedOptions = attempt.options.all()
    questions = Question.objects.filter(competition=competition.id, subject=attempt.subject, grade=request.user.grade)
    response_questions = []

    for question in questions:
        response_question = {
            'id': question.id,
            'text': question.text,
        }

        options = list(Option.objects.filter(question=question))
        random.shuffle(options)

        response_options = []

        for option in options:
            response_option = {
                'id': option.id,
                'text': option.text,
                'is_correct': option.is_correct 
            }
            response_option['is_selected'] = True if option in selectedOptions else False
            response_options.append(response_option)

        response_question['options'] = response_options
        response_questions.append(response_question)

    context = {
        'attempt': attempt,
        'competition': competition,
        'questions': response_questions
    }

    return render(request, 'competition/getAttempt.html', context)



def chop_microseconds(time_difference):
    seconds_without_microseconds = int(time_difference.total_seconds())
    return timedelta(seconds=seconds_without_microseconds)\
