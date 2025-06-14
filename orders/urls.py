from django.urls import path

from .views import order_create, order_created

urlpatterns = [
    path('create/', order_create, name='order_create'),
    path('order_created/<int:order_id>', order_created, name='order_created'),
]
