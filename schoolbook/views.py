from django.shortcuts import render
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from .models import SchoolBook, Module, Lesson


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

@cache_page(CACHE_TTL)
def Schoolbooks(request):
    schoolbooks = SchoolBook.objects.filter(grade=request.user.grade.id)
    context = {
        'schoolbooks': schoolbooks
    }
    return render(request, 'schoolbook/schoolbooks.html', context)

def Schoolbook(request, school_book_slug):
    schoolbook = SchoolBook.objects.get(slug=school_book_slug)
    modules = Module.objects.filter(school_books__id=schoolbook.id)
    response_modules = []
    
    for module in modules:
        lessons = Lesson.objects.filter(module=module.id)
        response_modules.append({
            'title': module.title,
            'lessons': lessons
        })

    context = {
        'schoolbook': schoolbook,
        'modules': response_modules
    }
    
    return render(request, 'schoolbook/schoolbook.html', context)

def LessonView(request, lesson_slug):
    lesson = Lesson.objects.get(slug=lesson_slug)
    context = {
        'lesson': lesson
    }
    return render(request, 'schoolbook/lesson.html', context)