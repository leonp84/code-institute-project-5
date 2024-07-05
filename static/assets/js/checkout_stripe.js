// This code has been largely copied and adopted from the Stripe Documentation at:
// https://docs.stripe.com/payments/accept-a-payment

$(function () {
  const stripe = Stripe(
    'pk_test_51PWFSE06QAYmePn9nZGc82dNrulo8BxwaoQOoRoThpMIXYqhKFlfjgTypOvHaRu8qXAGjdomy9ls9ZKg5NW8B0HQ009DaX1vWC'
  );
  let amountToPay = $('#amount-to-pay').text().replace(',', '');
  amountToPay += '00';
  amountToPay = parseInt(amountToPay);

  initialize(amountToPay, stripe);
  checkStatus();

  document.querySelector('#payment-form');
  $('#payment-form').on('submit', function (e) {
    handleSubmit(e, stripe);
  });
});

async function initialize(amountToPay, stripe) {
  const response = await fetch('/checkout/checkout_data/', {
    method: 'POST',
    dataType: 'json',
    headers: { 'Content-Type': 'application/json', 'X-CSRFToken': CSRF_TOKEN },
    body: JSON.stringify({ amount: amountToPay }),
  });
  const { clientSecret } = await response.json();
  const appearance = {
    theme: 'stripe',
  };
  let elements = stripe.elements({ appearance, clientSecret });
  //
  const paymentElementOptions = {
    layout: 'tabs',
  };

  const paymentElement = elements.create('payment', paymentElementOptions);
  paymentElement.mount('#payment-element');
}

async function handleSubmit(e, stripe) {
  e.preventDefault();
  $('#submit-order').html(
    `<span>Processing your payment...</span>
        <div class="spinner-border spinner-border-sm" role="status"></div>`
  );
  $('#submit-order').attr('disabled', true);
  let returnUrl =
    'https://' + window.location.hostname + '/checkout/order_confirmation/';

  const { error } = await stripe.confirmPayment({
    elements,
    confirmParams: {
      return_url: returnUrl,
    },
  });

  if (error.type === 'card_error' || error.type === 'validation_error') {
    showMessage(error.message);
    $('#submit-order').html('Retry Secure Payment');
    $('#submit-order').attr('disabled', false);
  } else {
    showMessage('An unexpected error occurred.');
    $('#submit-order').html('Retry Secure Payment');
    $('#submit-order').attr('disabled', false);
  }
}

async function checkStatus() {
  const clientSecret = new URLSearchParams(window.location.search).get(
    'payment_intent_client_secret'
  );

  if (!clientSecret) {
    return;
  }

  const { paymentIntent } = await stripe.retrievePaymentIntent(clientSecret);

  switch (paymentIntent.status) {
    case 'succeeded':
      showMessage('Payment succeeded!');
      break;
    case 'processing':
      showMessage('Your payment is processing.');
      break;
    case 'requires_payment_method':
      showMessage('Your payment was not successful, please try again.');
      break;
    default:
      showMessage('Something went wrong.');
      break;
  }
}

// ------- UI helpers -------

function showMessage(messageText) {
  const messageContainer = document.querySelector('#payment-message');

  messageContainer.classList.remove('hidden');
  messageContainer.textContent = messageText;

  setTimeout(function () {
    messageContainer.classList.add('hidden');
    messageContainer.textContent = '';
  }, 6000);
}
