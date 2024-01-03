from django.shortcuts import render
from .models import SchoolBook, Module, Lesson

def Schoolbooks(request):
    schoolbooks = SchoolBook.objects.filter(grade=request.user.grade.id)
    context = {
        'schoolbooks': schoolbooks
    }
    return render(request, 'schoolbook/schoolbooks.html', context)

def Schoolbook(request, school_book_id):
    schoolbook = SchoolBook.objects.get(id=school_book_id)
    modules = Module.objects.filter(school_books__id=school_book_id)
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

def LessonView(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    context = {
        'lesson': lesson
    }
    return render(request, 'schoolbook/lesson.html', context)