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
        event_dict = event.to_dict()
        intent = event_dict['data']['object']
        # Create delay for 'order_confirmation' view to complete
        time.sleep(5)
        # Check if the order has already been created at 'order_confirmation'
        pid = intent['id']
        if Order.objects.filter(stripe_pid=pid).exists():
            print('It has been found!')
            pass
        else:
            # If not, proceed fulfill by redirecting to the view
            print('It has NOT been found!')
            return HttpResponseRedirect(reverse(
                'order_confirmation', args=[pid]))
    else:
        print('EVENT = {}'.format(event.type))

    return HttpResponse(status=200)
