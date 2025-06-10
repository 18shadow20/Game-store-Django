from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from .forms import RegisterForm
from orders.models import Order

def login_view(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)

        if user is not None:
            user_login(request, user)
            return redirect('profile_views')
        return render(request, 'user/login.html', {'error': 'Неверный логин или пароль'})


    return render(request, 'user/login.html')


def register_view(request):
    if request.method == 'POST':

        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_login(request, user)
            return redirect('main')
    else:
        form = RegisterForm()
    return render(request, 'user/register.html', {'form': form})


@login_required
def profile_views(request):
    return render(request, 'user/profile.html', {'user':request.user})