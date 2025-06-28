from .models import Genre

def genres_context(request):
    genres = Genre.objects.all()
    return {'genres': genres,}