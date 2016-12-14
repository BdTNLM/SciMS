from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=200)
    def __str__(self):
        return self.nom

class Article(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField('date published')
    content = models.TextField()
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    def test(self):
        return self.title