from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login, name='login'),
    path('register/', views.Register, name='register'),
    path('settings/', views.Settings, name='settings'),
    path('logout/', views.Logout, name='logout'),
]