
from django import forms

from .models import Produit

class ProduitForm(forms.ModelForm):

    class Meta:
        model= Produit
        fields=('nom','designation','date_achat','date_peremption','prix','quantite')
        