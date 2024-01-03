from django.urls import path
from . import views

urlpatterns = [
    path('', views.Schoolbooks, name='schoolbooks'),
    path('<str:school_book_id>', views.Schoolbook, name='schoolbook'),
    path('lesson/<str:lesson_id>', views.Lesson, name='lesson')
]