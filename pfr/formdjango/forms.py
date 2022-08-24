
from django import forms

from .models import Produit

class ProduitForm(forms.ModelForm):
    date_achat = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), 
                                 input_formats=('%d/%m/%Y',))
    date_peremption = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), 
                                 input_formats=('%d/%m/%Y',))

    class Meta:
        model= Produit
        fields=('nom','designation','vendeur','date_achat','date_peremption','prix','quantite')
