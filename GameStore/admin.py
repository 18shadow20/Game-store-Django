from django.contrib import admin
from .models import Game, Genre, Tag, Comment, MainCategories, GameKey

# Register your models here.

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','is_available',)
    search_fields = ('name',)
    list_filter = ('is_available', 'genre','tag')
    prepopulated_fields = {'slug':('name',)}

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','game','text', 'created_at')


@admin.register(MainCategories)
class MainCategoriestAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(GameKey)
class GameKeyAdmin(admin.ModelAdmin):
    list_display = ('game','key', 'is_used')