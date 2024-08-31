from django.urls import path
from . import views

urlpatterns = [
    path('', views.competitions, name='competitions'),
    path('<slug:competition_slug>', views.get_competition, name='competition'),
    path('attempt/<slug:competition_slug>/<slug:subject_slug>', views.StartAttempt, name='attempt'),
    path('attempt/<str:attempt_id>', views.StartAttempt, name='get_attempt'),
    path('finish_attempt/<str:attempt_id>', views.FinishAttempt, name='finish_attempt'),
    path('get_attempt/<str:competition_slug>', views.GetAttempt, name='get_attempt')
]