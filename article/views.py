from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Article

def Articles(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'article/articles.html', context)


@login_required
def NewArticle(request):
    pass


def Get(request, article_slug):
    article = Article.objects.get(slug=article_slug)
    context = {
        'article': article
    }
    return render(request, 'article/article.html', context)

