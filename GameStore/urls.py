from django.urls import path
from .views import Main, Catalog, detail

urlpatterns = [
    path('', Main, name='main'),
    path('catalog', Catalog, name='catalog'),
    path('catalog/<int:num>', detail, name='game_detail'),
]