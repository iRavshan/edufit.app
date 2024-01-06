from django.urls import path
from . import views

urlpatterns = [
    path('', views.Schoolbooks, name='schoolbooks'),
    path('<slug:school_book_slug>', views.Schoolbook, name='schoolbook'),
    path('lesson/<slug:lesson_slug>', views.LessonView, name='lesson')
]