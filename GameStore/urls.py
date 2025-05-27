from django.urls import path
from .views import Main, Catalog

urlpatterns = [
    path('', Main),
    path('catalog', Catalog),
]