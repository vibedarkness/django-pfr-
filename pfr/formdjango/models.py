from django.db import models

# Create your models here.

class Produit(models.Model):

    nom=models.CharField(max_length=50)
    designation=models.TextField()
    vendeur=models.CharField(max_length=50)
    date_achat=models.DateField()
    date_peremption=models.DateField()
    prix=models.IntegerField()
    quantite=models.IntegerField()