$(function () {
  // Add Eventlistener for when customer click on additional product images
  $('.watch-extra-images').on('click', function () {
    let newImage = $(this).attr('src');
    $('.main-product-image').attr('src', newImage);
    $('#modal-image').attr('src', newImage);
    $('.watch-extra-images').css('border', '1px solid black');
    $(this).css('border', '1px solid rgb(208, 177, 20)');
  });

  // Show an enlarged image model when user clicks on main product image
  $('.main-product-image').on('click', function () {
    $('#largeImageModal').modal('show');
  });
  // Add Eventlistener for when product added to shopping bag
  $('#buy-button').on('click', function () {
    $('#buy-button').html(
      `<span>Adding...</span>
        <div class="spinner-border spinner-border-sm" role="status"></div>`
    );
    $('#buy-button').attr('disabled', true);
    $('#buy-button').css('background-color', 'grey');

    setTimeout(() => {
      addItemToBag();
    }, '1500');
  });
  // Add Eventlistener from when customer submits new product message
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

  // Bookmark Icon
  $('#bookmark-icon').on('click', addBookmarkedItem);
});

/**
 * Send AJAX request to server to update shopping bag and update the shopping bag contents number in the header
 */
function addItemToBag() {
  // AJAX POST Request to update shopping bag
  let productId = parseInt($('#product-id').text());
  $.ajax({
    url: '/checkout/add_item_to_bag/',
    type: 'POST',
    data: JSON.stringify({
      product_id: productId,
    }),
    dataType: 'json',
    headers: {
      'X-Requested-With': 'XMLHttpRequest',
      'X-CSRFToken': CSRF_TOKEN,
    },

    success: function (response) {
      if (response.status === 'ok') {
        // Add Item to Cart
        let itemsInCart = parseInt($('.bag-items-number').first().text());
        itemsInCart += 1;
        $('.bag-items-number').text(itemsInCart);
        $('.bag-items-number').show();

        $('#buy-button').html('Add an additional item');
        $('#buy-button').attr('disabled', false);
        $('#buy-button').css('background-color', '#212529');
        let addedToCartToast = bootstrap.Toast.getOrCreateInstance(
          $('#added-to-cart-toast')
        );
        addedToCartToast.show();
      } else {
        // Inform Customer that Product Limit Reached (max 3 per product)
        $('#buy-button').html('Add an additional item');
        let productLimit = bootstrap.Toast.getOrCreateInstance(
          $('#product-limit-toast')
        );
        productLimit.show();
      }
    },
    error: function (xhr, status, error) {
      console.error(error);
    },
  });
}

/**
 * Created new CustomerMessage model instance by sending information to backend via AJAX
 */
function sendCustomerMessage() {
  $('#send-message-button').html('Send Message');
  $('#send-message-button').attr('disabled', false);

  // Get form info for AJAX POST request
  let customerName = $('#name-input').val();
  let customerEmail = $('#email-input').val();
  let productName = $('#product-name').val();
  let productRef = $('#product-ref').val();
  let customerMessage = $('#customer-message').val();

  // AJAX POST Request
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

/**
 * Update Customer wishlist (if they are logged in)
 */
function addBookmarkedItem() {
  // AJAX POST Request to update Bookmarked Items
  let productId = parseInt($('#product-id').text());
  let wishListToast = bootstrap.Toast.getOrCreateInstance(
    $('#wish-list-toast')
  );
  $.ajax({
    url: '/my_account/add_bookmarked_item/',
    type: 'POST',
    data: JSON.stringify({
      product_id: productId,
    }),
    dataType: 'json',
    headers: {
      'X-Requested-With': 'XMLHttpRequest',
      'X-CSRFToken': CSRF_TOKEN,
    },
    success: function (response) {
      if (response.status === 'ok') {
        console.log(response.message);
        $('#wish-list-toast .toast-body').text(response.message);
        $('#bookmark-icon').toggleClass('fa-regular');
        $('#bookmark-icon').toggleClass('fa-solid');
        wishListToast.show();
      } else {
        // If customer does not have an account: Display 'create-account-modal'
        $('#create-account-modal').modal('show');
      }
    },
    error: function (xhr, status, error) {
      console.error(error);
    },
  });
}
