from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
import stripe
from orders.models import Order
from django.conf import settings
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from GameStore.models import GameKey

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION


@csrf_exempt
def createPayment(request):
    order_id = request.session.get('order_id', None)

    order = get_object_or_404(Order, id=order_id)

    success_url = request.build_absolute_uri(reverse('completed'))
    cancel_url = request.build_absolute_uri(reverse('canceled'))

    session_data = {
        'mode':'payment',
        'client_reference_id':order.id,
        'success_url':success_url,
        'cancel_url':cancel_url,
        'payment_method_types':['card'],
        'line_items':[],
    }

    for item in order.items.all():
        session_data['line_items'].append({
            'price_data':{
                'currency':'byn',
                'unit_amount':int(item.price * 100),
                'product_data':{
                    'name': item.game.name,
                },
            },
            'quantity':item.quantity,
        })

    session = stripe.checkout.Session.create(**session_data)
    return redirect(session.url, code=303)


def payment_completed(request):
    return render(request, 'payment/completed.html')

def payment_canceled(request):
    return render(request, 'payment/canceled.html' )



@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')

    try:
        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            settings.STRIPE_WEBHOOK_SECRET
        )
    except stripe.error.SignatureVerificationError:
        return HttpResponse('Invalid signature')

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        order_id = session.get('client_reference_id')


        try:
            order = Order.objects.get(id=order_id)
            order.paid = True
            order.save()

            # выдать ключ каждому товару
            for item in order.items.all():
                game = item.game
                for _ in range(item.quantity):
                    key = GameKey.objects.filter(game=game, is_used=False).first()
                    if key:
                        key.is_used = True
                        key.save()

                        # отправка ключа
                        send_mail(
                            subject='Ваш ключ игры',
                            message=f'Спасибо за покупку {game.name}!\nВаш ключ: {key.key}',
                            from_email=settings.DEFAULT_FROM_EMAIL,
                            recipient_list=[order.email],
                         )
        except Order.DoesNotExist:
            print("Заказ не найден в webhook")

    return HttpResponse(status=200)






