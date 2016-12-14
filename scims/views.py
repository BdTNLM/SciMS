from django.shortcuts import render
from django.http import HttpResponse
from .models import Article,Categorie,Sous_Categorie
from django.http import Http404
from .templatetags.scims_extras import addstr
from django.shortcuts import get_object_or_404
# Create your views here.

def index(request):
    liste_article = Article.objects.order_by('date')[:5]
    liste_categorie = Categorie.objects.all()
    liste_sous_categorie=Sous_Categorie.objects.all()
    return render(request, 'scims/index.html', {'liste_article': liste_article,'liste_categorie':liste_categorie,'liste_sous_categorie':liste_sous_categorie})

def register(request):
    return None

def article(request, article_name):
    article=get_object_or_404(Article,title=article_name)
    return render(request, 'scims/article.html', {'article': article})
def categorie(request,categorie):
    return None