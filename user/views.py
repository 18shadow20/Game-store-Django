from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from .forms import RegisterForm

def login_view(request):

    if request.method == 'POST':

        login = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(request, username = login, password = password)

        if user is not None:
            user_login(request, user)
            return redirect('/')


    return render(request, 'user/login.html')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'user/register.html', {'form': form})