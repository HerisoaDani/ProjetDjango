from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

class Transaction(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

class ObjectifFinancier(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    montant_cible = models.DecimalField(max_digits=10, decimal_places=2)
    date_limite = models.DateField()

class Recommandation(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
