from django.db import models
from GameStore.models import Game
from django.contrib.auth import get_user_model

user = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(to=user, on_delete=models.SET_NULL, blank=True, null=True, default=None)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return f'Заказ: {self.id}'

    def get_total_cost(self):
        return sum(i.get_cost() for i in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    game = models.ForeignKey(Game, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} из {self.game.name}'

    def get_cost(self):
        return self.price * self.quantity