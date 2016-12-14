from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.http import Http404
from .templatetags.scims_extras import addstr
from django.shortcuts import get_object_or_404
# Create your views here.

def index(request):
    listeArticle = Article.objects.order_by('date')[:5]
    return render(request, 'scims/index.html', {'listeArticle': listeArticle})

def register(request):
    return None

def article(request, categorie, article_name):
    article=get_object_or_404(Article,title=article_name)
    return render(request, 'scims/article.html', {'article': article})