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
    if request.user.is_authenticated:
        viewers = article.viewers.all()
        if not request.user in viewers:
            article.viewers.add(request.user)
            article.save()
    context = {
        'article': article
    }
    return render(request, 'article/article.html', context)

