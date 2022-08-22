from importlib.resources import path
from unicodedata import name
from django.urls import path,include


from .views import index


urlpatterns = [
    path('', index,name="index" )
]
