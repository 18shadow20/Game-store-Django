from django.shortcuts import render, redirect, get_object_or_404
from GameStore.models import Game
from .cart import Cart
from django.views.decorators.http import require_POST
from .forms import CartAddGameForm


@require_POST
def cart_add(request, game_id):
    cart = Cart(request)
    game = get_object_or_404(Game, id = game_id)
    form = CartAddGameForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(game=game, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart_detail')


@require_POST
def cart_remove(request, game_id):
    cart = Cart(request)
    game = get_object_or_404(Game, id = game_id)
    cart.remove(game)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    context = {
        'cart':cart,
        'cart_items':list(cart),
        'cart_total':cart.get_total_price()
    }
    return render(request, 'cart/detail.html', context)

