from django.urls import path
from .views import Main, Catalog, detail

urlpatterns = [
    path('', Main, name='main'),
    path('catalog', Catalog, name='catalog'),
    path('catalog/<slug:slug>', detail, name='game_detail'),
]