from django.db import models
from django.db.models import SET_DEFAULT, SET_NULL
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=50,unique=True, verbose_name='Название игры')
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField( max_digits=6, decimal_places=2 ,verbose_name="цена")
    image = models.ImageField(upload_to='media/games/')
    genre = models.ManyToManyField('Genre', )
    tag = models.ManyToManyField('Tag',blank=True)
    is_available = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('GameStore/game_detail',
                       args=[self.slug])

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(to=User, blank=True, on_delete=SET_NULL, null=True)
    game = models.ForeignKey(to=Game, on_delete=SET_NULL, null=True, blank=True)
    text = models.TextField(verbose_name='Отзыв')
    created_at = models.DateTimeField(auto_now_add=True)
