from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categorie(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
        return self.nom

class Article(models.Model):
    title = models.CharField(max_length=200,primary_key=True)
    date = models.DateTimeField('date published')
    content = models.TextField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    redacteur = models.ForeignKey(User,default=None)

    def __str__(self):
        return self.title + ":::"  + self.date.__str__() + ":::" + self.redacteur.username
