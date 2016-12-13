from django.db import models

# Create your models here.

class Categorie(models.Model):
    nom = models.CharField(max_length=200)

class Article(models.Model):
    title = models.CharField(max_length=200,primary_key=True)
    date = models.DateTimeField('date published')
    content = models.TextField()
    categorie = models.ForeignKey(Categorie)
