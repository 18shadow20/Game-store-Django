from django.contrib import admin
from .models import Order, OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name','email','paid','created', 'update',)
    search_fields = ('first_name',)
    list_filter = ('paid','created', 'update',)
