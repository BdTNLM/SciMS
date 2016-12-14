from django.contrib import admin
from .models import Categorie,Article,Sous_Categorie

# Register your models here.
admin.site.register(Categorie)
admin.site.register(Article)
admin.site.register(Sous_Categorie)