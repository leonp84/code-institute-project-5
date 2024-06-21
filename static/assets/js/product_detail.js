$(function () {
  let productId = parseInt($('#product-id').text());
  $('.watch-extra-images').on('click', function () {
    updateMainProductImage();
  });

  $('.main-product-image').on('click', function () {
    $('#largeImageModal').modal('show');
    window.localStorage.clear();
  });

  $('#buy-button').on('click', function () {
    $('#buy-button').html(
      `<span>Adding...</span>
        <div class="spinner-border spinner-border-sm" role="status"></div>`
    );
    $('#buy-button').attr('disabled', true);
    $('#buy-button').css('background-color', 'grey');

    setTimeout(() => {
      addItemToBag();
    }, '3000');
  });

  $('#customer-message-form').on('submit', function (e) {
    e.preventDefault();
    $('#send-message-button').html(
      `<span>Sending...</span>
          <div class="spinner-border spinner-border-sm" role="status"></div>`
    );
    $('#send-message-button').attr('disabled', true);
    $('#enquire-button').attr('disabled', true);

    setTimeout(() => {
      sendCustomerMessage();
    }, '3000');
  });
});

/**
 *
 */
function addItemToBag() {
  if (window.localStorage.getItem('shoppingBagTotal') === null) {
    window.localStorage.setItem('shoppingBagTotal', 1);
    $('.bag-items-number').text('1');
    $('.bag-items-number').show();
  } else {
    itemsInCart = parseInt(window.localStorage.getItem('shoppingBagTotal'));
    itemsInCart += 1;
    window.localStorage.setItem('shoppingBagTotal', itemsInCart);
    $('.bag-items-number').text(itemsInCart);
  }
  $('#buy-button').html('Add an additional item');
  $('#buy-button').attr('disabled', false);
  $('#buy-button').css('background-color', '#212529');
  let addedToCartToast = bootstrap.Toast.getOrCreateInstance(
    $('#added-to-cart-toast')
  );
  addedToCartToast.show();
}

/**
 *
 */
function updateMainProductImage() {
  let newImage = $(this).attr('src');
  $('.main-product-image').attr('src', newImage);
  $('#modal-image').attr('src', newImage);
  $('.watch-extra-images').css('border', '1px solid black');
  $(this).css('border', '1px solid rgb(208, 177, 20)');
}

/**
 *
 */
function sendCustomerMessage() {
  $('#send-message-button').html('Send Message');
  $('#send-message-button').attr('disabled', false);

  // Get form info for AJAX POST request
  customerName = $('#name-input').val();
  customerEmail = $('#email-input').val();
  productName = $('#product-name').val();
  productRef = $('#product-ref').val();
  customerMessage = $('#customer-message').val();

  // AJAX POST Request
  // The CSFR_TOKEN variable below is provided at the bottom of the respective HTML file
  $.ajax({
    url: '/product/customer_product_message/',
    type: 'POST',
    data: JSON.stringify({
      customer_name: customerName,
      customer_email: customerEmail,
      product_name: productName,
      product_ref: productRef,
      customer_message: customerMessage,
    }),
    dataType: 'json',
    headers: {
      'X-Requested-With': 'XMLHttpRequest',
      'X-CSRFToken': CSRF_TOKEN,
    },
    success: function (response) {
      console.log(response.message);
    },
    error: function (xhr, status, error) {
      console.error('Error:', error);
    },
  });

  $('#contact-us-modal').modal('hide');
  let messageSentToast = bootstrap.Toast.getOrCreateInstance(
    $('#message-sent-toast')
  );
  messageSentToast.show();
}
