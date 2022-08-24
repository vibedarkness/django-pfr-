
from multiprocessing import context
from django.shortcuts import render
from django.contrib import messages
from .forms import ProduitForm

from .models import Produit

# Create your views here.




def index(request):
    messages=""
    form = ProduitForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=ProduitForm()
        messages="votre produits a était bien ajouter"

    return render(request, 'index.html', {'form':form,'message':messages})

    # return render (request, 'index.html')


def tableau(request):

    prod=Produit.objects.all()

    if request.method== "GET":
        name=request.GET.get("recherche")
        if name is not None:
            prod=Produit.objects.filter(nom__icontains=name)

    context={
         'prod':prod,
    }

    return render(request,'tableau.html',context)


# def ajout_produit(request):

