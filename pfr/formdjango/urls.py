from importlib.resources import path
from unicodedata import name
from django.urls import path,include


from .views import index,tableau


urlpatterns = [
    path('', index,name="index" ),
    path('tableau/',tableau,name="tableau" ),
]
