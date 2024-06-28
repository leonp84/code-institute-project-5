from django.conf import settings
from django.shortcuts import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from checkout.models import Order
import time
import stripe
import json


@csrf_exempt
def webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET # noqa

    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Event.construct_from(
          json.loads(payload), sig_header, stripe.api_key
        )
    except ValueError as e:
        print(e)
        return HttpResponse(status=400)

    # Handle the event
    if event.type == 'payment_intent.succeeded':
        # Create delay for 'order_confirmation' view to complete
        time.sleep(5)
        # Check if the order has already been created at 'order_confirmation'
        pid = event['payment_intent']
        if Order.objects.filter(stripe_pid=pid).exists():
            pass
        else:
            # If not, proceed to complete order by redirecting to view
            return HttpResponseRedirect(reverse('order_payment', args=[pid]))
    else:
        print('EVENT = {}'.format(event.type))

    return HttpResponse(status=200)
