from django.db import models
from django.db.models import SET_NULL
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
    main_categories = models.ManyToManyField('MainCategories', blank=True)
    release_date = models.DateField(verbose_name='Дата издания',blank=True)
    publisher = models.CharField(max_length=50, verbose_name='Издатель',blank=True)


    def get_absolute_url(self):
        return reverse('GameStore/game_detail',
                       args=[self.slug])

    def __str__(self):
        return self.name

class GameImage(models.Model):
    game = models.ForeignKey(Game, related_name='game_gallery', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/game_gallery/')

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class MainCategories(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class GameKey(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='key')
    key = models.CharField(max_length=100, unique=True)
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.game.name} - {'использован' if self.is_used else 'доступен'}'


class Comment(models.Model):
    user = models.ForeignKey(to=User, blank=True, on_delete=SET_NULL, null=True)
    game = models.ForeignKey(to=Game, on_delete=SET_NULL, null=True, blank=True)
    text = models.TextField(verbose_name='Отзыв')
    created_at = models.DateTimeField(auto_now_add=True)

