from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_articles, name='articles'),
    path('new', views.new_article, name='new_article'),
    path('<slug:article_slug>', views.get_article, name='article'),
]