from django.shortcuts import render, get_object_or_404
from .models import Game, Genre, Tag
from django.core.paginator import Paginator

# Create your views here.
def Catalog(request):
    game = Game.objects.all()
    genre = Genre.objects.all()
    tag = Tag.objects.all()
    paginator = Paginator(game, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'GameStore/catalog.html', {
        'game':game,
        'genre':genre,
        'tag':tag,
        'page_obj': page_obj
    })

def Main(request):
    genre = Genre.objects.all()
    return render(request, 'GameStore/main.html', context={'genre':genre})


def detail(request, slug):
    game = get_object_or_404(Game, slug__iexact = slug)
    return render(request, 'GameStore/detail.html', context={'game':game})


