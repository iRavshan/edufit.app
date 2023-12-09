from django.urls import path
from . import views

urlpatterns = [
    path('', views.Rating, name='rating')
]