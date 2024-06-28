$(function () {
  $('#logo').on('click', function (e) {
    e.preventDefault();
    testWebhook();
  });

  if (parseInt($('.bag-items-number').first().text()) !== 0) {
    $('.bag-items-number').show();
  }

  // Initialize all Bootstrap Tooltips on page
  var tooltipTriggerList = [].slice.call(
    document.querySelectorAll('[data-bs-toggle="tooltip"]')
  );
  var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
  });

  allTextInputs = document.body.getElementsByTagName('input');
  for (i = 0; i < allTextInputs.length; i++) {
    allTextInputs[i].addEventListener('invalid', (e) => {
      e.target.classList.add('error');
      let errorMsg = document.createElement('div');
      errorMsg.innerHTML = `<span>This input is not valid</span>`;
      errorMsg.classList.add('error');
      e.target.parentNode.appendChild(errorMsg);
    });
  }

  // Eventlistener for search icon to reveal search bar
  $('.search-icon').on('click', function (e) {
    e.preventDefault();
    $('#search-box').toggle();
    $('#search-box').find('input').focus();
  });

  $('#search-scrolling-bar').on('click', function (e) {
    $('#search-box').toggle();
    $('#search-box').find('input').focus();
  });
});

function testWebhook() {
  let content = body();
  $.ajax({
    url: '/checkout/webhook/',
    type: 'POST',
    data: JSON.stringify({
      content: content,
    }),
    dataType: 'json',
    headers: {
      'X-Requested-With': 'XMLHttpRequest',
    },
    success: function (response) {
      if (response.status === 'ok') {
        console.log(response.message);
      }
    },
    error: function (xhr, status, error) {
      console.error(error);
    },
  });
}

function body() {
  let body = {
    id: 'evt_3PWdJd06QAYmePn91gMX4yOh',
    object: 'event',
    api_version: '2024-06-20',
    created: 1719575472,
    data: {
      object: {
        id: 'pi_3PWdJd06QAYmePn91aLLJ9GC',
        object: 'payment_intent',
        amount: 610000,
        amount_capturable: 0,
        amount_details: {
          tip: {},
        },
        amount_received: 610000,
        application: null,
        application_fee_amount: null,
        automatic_payment_methods: {
          allow_redirects: 'always',
          enabled: true,
        },
        canceled_at: null,
        cancellation_reason: null,
        capture_method: 'automatic_async',
        client_secret:
          'pi_3PWdJd06QAYmePn91aLLJ9GC_secret_qHvJcf2j1In3rKSfsyRNBptT7',
        confirmation_method: 'automatic',
        created: 1719575409,
        currency: 'usd',
        customer: null,
        description: null,
        invoice: null,
        last_payment_error: null,
        latest_charge: 'ch_3PWdJd06QAYmePn91wE1CLXA',
        livemode: false,
        metadata: {},
        next_action: null,
        on_behalf_of: null,
        payment_method: 'pm_1PWdKd06QAYmePn91fUnvJDY',
        payment_method_configuration_details: {
          id: 'pmc_1PWdIX06QAYmePn9Ig8RmHPp',
          parent: null,
        },
        payment_method_options: {
          card: {
            installments: null,
            mandate_options: null,
            network: null,
            request_three_d_secure: 'automatic',
          },
          link: {
            persistent_token: null,
          },
        },
        payment_method_types: ['card', 'link'],
        processing: null,
        receipt_email: null,
        review: null,
        setup_future_usage: null,
        shipping: null,
        source: null,
        statement_descriptor: null,
        statement_descriptor_suffix: null,
        status: 'succeeded',
        transfer_data: null,
        transfer_group: null,
      },
    },
    livemode: false,
    pending_webhooks: 1,
    request: {
      id: 'req_lCyte8Tt6H9nMe',
      idempotency_key: '2d700844-e763-427b-8c2f-17bcc2148e01',
    },
    type: 'payment_intent.succeeded',
  };
  return body;
}
