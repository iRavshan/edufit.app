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
    context = {
        'schoolbook': schoolbook
    }
    return render(request, 'schoolbook/schoolbook.html')

def Lesson(request):
    return render(request, 'schoolbook/lesson.html')