from django.db import models

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название игры')
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField( max_digits=6, decimal_places=2 ,verbose_name="цена")
    image = models.ImageField(upload_to='media/games/')
    genre = models.ManyToManyField('Genre', )
    tags = models.ManyToManyField('Tag',)
    is_available = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Tag(models.Model):
    name = models.CharField(max_length=50)