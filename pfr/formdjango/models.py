from django.db import models

# Create your models here.

class Produit(models.Model):

    nom=models.CharField(max_length=50)
    designation=models.TextField()
    vendeur=models.CharField(max_length=50)
    date_achat=models.DateField(auto_now=False, auto_now_add=False)
    date_peremption=models.DateField(auto_now=False, auto_now_add=False)
    prix=models.DecimalField (max_digits=5, decimal_places=4)
    quantite=models.IntegerField()