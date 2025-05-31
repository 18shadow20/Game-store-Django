from django.urls import path
from django.contrib.auth import views as auth_views
from .views import login_view, register_view

urlpatterns = [
    path('login/', login_view, name='login_view'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login_view'), name='logout_view'),
    path('register/', register_view, name='register_view')

]