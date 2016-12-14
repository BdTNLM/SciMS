from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.http import Http404
# Create your views here.

def index(request):
    listeArticle = Article.objects.order_by('date')[:5]
    return render(request, 'scims/index.html', {'listeArticle': listeArticle})

def register(request):
    return None


def article(request,article_name):
    try:
        article = Article.objects.get(pk=article_name)

    except Article.DoesNotExist:
        raise Http404("Question doesn't exist")
    return render(request, 'scims/article.html', {'article': article})