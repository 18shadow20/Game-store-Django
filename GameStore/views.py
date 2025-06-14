from django.shortcuts import render, get_object_or_404
from .models import Game, Genre, Tag
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def Catalog(request):
                #фильтры
    name_filt = request.GET.get('name_filt')
    genre_filt = request.GET.getlist('genre')
    tag_filt = request.GET.getlist('tag')
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')

    game = Game.objects.all()

    if name_filt:
        game = Game.objects.filter(Q(name__icontains = name_filt) | Q(description__icontains=name_filt))

    if genre_filt:
        game = game.filter(genre__id__in = genre_filt).distinct()

    if tag_filt:
        game = game.filter(tag__id__in = tag_filt).distinct()

    if price_min and price_max and price_min.isdigit() and price_max.isdigit():
        game = game.filter(price__range=(int(price_min), int(price_max)))
    elif price_min and price_min.isdigit():
        game = game.filter(price__gte = int(price_min))
    elif price_max and price_max.isdigit():
        game = game.filter(price__lte=int(price_max))

    genre = Genre.objects.all()
    tag = Tag.objects.all()
    paginator = Paginator(game, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    return render(request, 'GameStore/catalog.html', {
        'game':game,
        'genre':genre,
        'tag':tag,
        'page_obj': page_obj,
        'name_filt':name_filt,
        'genre_filt':list(map(int, genre_filt)),
        'tag_filt':list(map(int, tag_filt)),
        'price_min':price_min,
        'price_max':price_max,
    })

def Main(request):
    genre = Genre.objects.all()
    return render(request, 'GameStore/main.html', context={'genre':genre})


def detail(request, slug):
    game = get_object_or_404(Game, slug__iexact = slug)
    return render(request, 'GameStore/detail.html', context={'game':game})

