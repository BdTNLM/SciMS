from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categorie(models.Model):
    nom = models.CharField(max_length=200,unique=True)
    def __str__(self):
        return self.nom

class Sous_Categorie(models.Model):
    mere = models.ForeignKey(Categorie)
    nom = models.CharField(max_length=200,unique=True)
    def __str__(self):
        return self.nom

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200,unique=True)
    date = models.DateTimeField('date published')
    content = models.TextField()
    categorie = models.ForeignKey(Categorie)
    redacteur = models.ForeignKey(User,default=None)
    def __str__(self):
        return self.title + ":::"  + self.date.__str__() + ":::" + self.redacteur.username