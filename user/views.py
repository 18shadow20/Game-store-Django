from django.contrib.auth.decorators import login_required
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as user_login, get_user_model
from django.contrib import messages
from .forms import RegisterForm, CustomProfileForm
from orders.models import Order

User = get_user_model()

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
    editing = request.GET.get('edit') == 'true'

    if request.method == 'POST':
        form = CustomProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль изменен')
            return redirect('profile_views')
    else:
        form = CustomProfileForm(instance=request.user)
    return render(request, 'user/profile.html', {'user':request.user,
                                                                     'form':form,
                                                                     'editing':editing},
                                                                     )