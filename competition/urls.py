from django.urls import path
from . import views

urlpatterns = [
    path('', views.Competitions, name='competitions'),
    path('<str:id>', views.Get, name='competition'),
    path('attempt/<str:competition_id>/<str:subject_name>', views.StartAttempt, name='attempt'),
    path('attempt/<str:attempt_id>', views.StartAttempt, name='get_attempt'),
    path('finish_attempt/<str:attempt_id>', views.FinishAttempt, name='finish_attempt'),
    path('get_attempt/<str:competition_id>', views.GetAttempt, name='get_attempt')
]