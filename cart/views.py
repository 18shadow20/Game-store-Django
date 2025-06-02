from django.shortcuts import render, redirect, get_object_or_404
from GameStore.models import Game
from .cart import Cart

def cart_add(request, game_id):
    cart = Cart(request)
    game = get_object_or_404(Game, id = game_id)
    cart.add(game = game, quantity=1, update_quantity=True)
    return redirect('cart_detail')

def cart_remove(request, game_id):
    cart = Cart(request)
    game = get_object_or_404(Game, id = game_id)
    cart.remove(game)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})

