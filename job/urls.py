from django.urls import path
from . import views

urlpatterns = [
    path('', views.Jobs, name='jobs')
]