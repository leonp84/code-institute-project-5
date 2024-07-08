from django.conf import settings
from django.shortcuts import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import time
import stripe
import json
from checkout.models import Order


@csrf_exempt
def webhook(request):
    '''
    This view is called by Stripe at various times during the payment process.
    The webhook handler here only responds when stripe sends a
    'payment_intent.succeeded' webhook and checks to ensure the order has been
    fulfilled by checkout.views.order_confirmation. If not, this view serves as
    redundancy by redirecting to checkout.views.order_confirmation to complete
    the order and send the necessary confirmation emails to the customer.
    NOTE: Much of the code here was copied and adapted from the stripe
    documentation at https://docs.stripe.com/webhooks/quickstart
    '''
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET  # noqa

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
            pass
        else:
            # If not, proceed to fulfill by redirecting to the view
            return HttpResponseRedirect(reverse(
                'order_confirmation', args=[pid]))
    else:
        print('EVENT = {}'.format(event.type))

    return HttpResponse(status=200)
