from django.urls import path
from . import views

urlpatterns = ([
    path('completed/', views.payment_completed, name='completed'),
    path('canceled/', views.payment_canceled, name='canceled'),
    path('create/', views.createPayment, name='payment_create'),
    path('webhooks/', views.stripe_webhook, name='stripe_webhook'),
])