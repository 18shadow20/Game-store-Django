from django.shortcuts import render
from .models import Game, Genre, Tag

# Create your views here.
def Catalog(request):
    game = Game.objects.all()
    genre = Genre.objects.all()
    tag = Tag.objects.all()
    return render(request, 'GameStore/catalog.html', {
        'game':game,
        'genre':genre,
        'tag':tag,
    })

def Main(request):
    genre = Genre.objects.all()
    return render(request, 'GameStore/main.html', context={'genre':genre})
