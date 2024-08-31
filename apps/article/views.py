from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .repositories.article_repository import ArticleRepository


articleRepository = ArticleRepository()


def all_articles(request):
    context = {
        'articles': articleRepository.get_all()
    }
    return render(request, 'article/blog.html', context)


def get_article(request, article_slug):
    article = articleRepository.get_by_slug(article_slug)
    if request.user.is_authenticated:
        viewers = article.viewers.all()
        if not request.user in viewers:
            article.viewers.add(request.user)
            article.save()
    context = {
        'article': article
    }
    return render(request, 'article/article.html', context)


@login_required
def new_article(request):
    pass