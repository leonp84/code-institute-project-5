let currentTotal = $('#checkout-total').text();

$(function () {
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

  $('#add-watch-care-plan').change(function () {
    $('#add-watch-care-plan').attr('disabled', 'true');
    currentPrice = parseInt($('#checkout-total').text().replace(',', ''));
    if (this.checked) {
      newPrice = parseInt(currentPrice + (currentPrice / 100) * 2.5);
    } else {
      newPrice = currentTotal;
    }
    $('#checkout-total').html(
      `<span>Updating...</span>
      <div class="spinner-border spinner-border-sm" role="status"></div>`
    );
    setTimeout(() => {
      $('#add-watch-care-plan').removeAttr('disabled');
      $('#checkout-total').html(newPrice.toLocaleString());
    }, '1500');
  });

  $('.delete-item').on('click', function (e) {
    $('#checkout-total').html(
      `<span>Updating...</span>
      <div class="spinner-border spinner-border-sm" role="status"></div>`
    );
    e.preventDefault();
    $(this).parent().parent().parent().remove();
    setTimeout(() => {
      updatePrice();
    }, '1500');
  });
});

function updatePrice() {
  products = document.body.getElementsByClassName('product-id-js');
  let productsArr = [];
  for (i = 0; i < products.length; i++) {
    productsArr.push(products[i].innerText.replace(',', ''));
  }
  console.log(productsArr);

  prices = document.body.getElementsByClassName('product-price-js');
  let pricesArr = [];
  for (i = 0; i < prices.length; i++) {
    pricesArr.push(prices[i].innerText.replace(',', ''));
  }
  console.log(pricesArr);

  quantities = document.body.getElementsByClassName('qty-js');
  let quantitiesArr = [];
  for (i = 0; i < quantities.length; i++) {
    quantitiesArr.push(parseInt(quantities[i].value));
  }
  console.log(quantitiesArr);
  let totalPrice = 0;
  for (i = 0; i < prices.length; i++) {
    totalPrice += parseInt(quantitiesArr[i]) * parseInt(pricesArr[i]);
  }

  $('#checkout-total').html(totalPrice.toLocaleString());
  currentTotal = totalPrice.toLocaleString();

  // AJAX POST Request to update shopping bag
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
  newTotalItems = quantitiesArr.reduce((partialSum, a) => partialSum + a, 0);
  $('.bag-items-number').text(newTotalItems);
}
