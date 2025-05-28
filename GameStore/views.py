from django.shortcuts import render, get_object_or_404
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


def detail(request, num):
    game = get_object_or_404(Game, pk=num)
    return render(request, 'GameStore/detail.html', context={'game':game})