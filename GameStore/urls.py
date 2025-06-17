from django.urls import path
from . import views

urlpatterns = [
    path('catalog', views.Catalog, name='catalog'),
    path('catalog/<slug:slug>', views.detail, name='game_detail'),
    path('review/', views.reviews, name='reviews'),
    path('guarantees/', views.guarantees, name='guarantees'),
    path('how_to_buy/', views.how_to_buy, name='how_to_buy'),
    path('', views.Main, name='main'),

]