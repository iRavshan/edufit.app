from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('rating/', include('rating.urls')),
    path('competitions/', include('competition.urls')),
    path('', views.Home, name='home')
]
