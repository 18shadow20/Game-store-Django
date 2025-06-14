from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, game = item['game'], price = item['price'],
                                         quantity = item['quantity'])
            cart.clear()
            return redirect('order_created', order_id = order.id)
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order_create.html', {'cart':cart, 'form':form})


def order_created(request, order_id):
    return render(request, 'orders/order_created.html',{'order_id':order_id})