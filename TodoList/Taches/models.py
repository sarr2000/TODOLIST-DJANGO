from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# creation du modele taches


class Categorie(models.Model):
    nom_categorie = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_categorie


class Tache(models.Model):
    nom_tache =models.CharField(max_length=100)
    date = models.DateField(null='true', blank='True')
    heure_debut = models.TimeField(null='true', blank='True')
    heure_fin = models.TimeField(null='true', blank='True')
    choix_priorite=(
        ('faible',"Faible"),
        ('moyenne',"Moyenne"),
        ('haute',"Haute"),
    )
    priorite = models.CharField(max_length=20,choices=choix_priorite)
    choix_statut = (
        ('en attente', "En attente"),
        ('faite', "Faite"),
        ('en cours', "En cours"),
        ('à faire',"A faire"),
    )
    statut = models.CharField(max_length= 20,choices=choix_statut)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, null='true', blank='True')
    responsable = models.ForeignKey(User, on_delete=models.CASCADE, null='true',blank='True')
    commentaire = models.TextField()


    def __str__(self):
        return self.nom_tache




