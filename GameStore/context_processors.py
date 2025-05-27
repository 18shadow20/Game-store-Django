from .models import Genre

def genres_context(request):
    genre = Genre.objects.all()
    return {'genre': genre}