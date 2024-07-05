let currentTotal = $('#checkout-total').text();

$(function () {
  // Update total order price when customer change the quantity of any item in the shopping bag
  updatePrice();
  $('.qty-js').on('change', function () {
    $('#checkout-total').html(
      `<span>Updating...</span>
          <div class="spinner-border spinner-border-sm" role="status"></div>`
    );
    $('.qty-js').attr('disabled', 'true');
    setTimeout(() => {
      updatePrice();
      $('.qty-js').removeAttr('disabled');
    }, '2000');
  });

  // Check for when customer update their watch plan status
  $('#add-watch-care-plan').change(function () {
    let watchCarePlan = false;
    $('#add-watch-care-plan').attr('disabled', 'true');
    let currentPrice = parseInt($('#checkout-total').text().replace(',', ''));
    let newPrice = 0;
    if (this.checked) {
      newPrice = parseInt(currentPrice + (currentPrice / 100) * 2.5);
      watchCarePlan = true;
    } else {
      newPrice = currentTotal;
      watchCarePlan = false;
    }
    $('#checkout-total').html(
      `<span>Updating...</span>
      <div class="spinner-border spinner-border-sm" role="status"></div>`
    );

    // AJAX POST Request to update watch care plan status
    $.ajax({
      url: '/checkout/update_watch_care_plan/',
      type: 'POST',
      data: JSON.stringify({
        watch_care_plan: watchCarePlan,
      }),
      dataType: 'json',
      headers: {
        'X-Requested-With': 'XMLHttpRequest',
        'X-CSRFToken': CSRF_TOKEN,
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

    setTimeout(() => {
      $('#add-watch-care-plan').removeAttr('disabled');
      $('#checkout-total').html(newPrice.toLocaleString());
    }, '1500');
  });

  // Check for when customers remove items for the shopping bag
  $('.delete-item').on('click', function (e) {
    $('#checkout-total').html(
      `<span>Updating...</span>
      <div class="spinner-border spinner-border-sm" role="status"></div>`
    );
    e.preventDefault();
    $(this).parent().parent().parent().remove();
    setTimeout(() => {
      updatePrice();
    }, '100');
  });
});

/*
 * Dynamically update price when item deleted or quantity updated in the shopping bag.
 */
function updatePrice() {
  let products = document.body.getElementsByClassName('product-id-js');
  let productsArr = [];
  for (let i = 0; i < products.length; i++) {
    productsArr.push(products[i].innerText.replace(',', ''));
  }

  let prices = document.body.getElementsByClassName('product-price-js');
  let pricesArr = [];
  for (let i = 0; i < prices.length; i++) {
    pricesArr.push(prices[i].innerText.replace(',', ''));
  }

  let quantities = document.body.getElementsByClassName('qty-js');
  let quantitiesArr = [];
  for (let i = 0; i < quantities.length; i++) {
    quantitiesArr.push(parseInt(quantities[i].value));
  }
  let totalPrice = 0;
  for (let i = 0; i < prices.length; i++) {
    totalPrice += parseInt(quantitiesArr[i]) * parseInt(pricesArr[i]);
  }

  $('#checkout-total').html(totalPrice.toLocaleString());
  currentTotal = totalPrice.toLocaleString();
  console.log(currentTotal);
  // Disable checkout button if total is 0 (i.e. customer has removed all items from the shopping list)
  if (currentTotal === '0') {
    $('#proceed-to-checkout').attr('href', '#');
    $('#proceed-to-checkout').removeClass('btn-warning');
    $('#proceed-to-checkout').addClass('btn-secondary');
  }
  // AJAX POST Request to update shopping bag in server session
  $.ajax({
    url: '/checkout/update_shopping_bag/',
    type: 'POST',
    data: JSON.stringify({
      updated_products: productsArr,
      updated_quantities: quantitiesArr,
    }),
    dataType: 'json',
    headers: {
      'X-Requested-With': 'XMLHttpRequest',
      'X-CSRFToken': CSRF_TOKEN,
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
  let newTotalItems = quantitiesArr.reduce(
    (partialSum, a) => partialSum + a,
    0
  );
  $('.bag-items-number').text(newTotalItems);
}
