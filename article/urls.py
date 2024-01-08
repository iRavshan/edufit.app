from django.urls import path
from . import views

urlpatterns = [
    path('', views.Articles, name='articles'),
    path('new', views.NewArticle, name='new_article'),
    path('<slug:article_slug>', views.Get, name='article'),
]