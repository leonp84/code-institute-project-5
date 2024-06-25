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
});

function updatePrice() {
  prices = document.body.getElementsByClassName('product-price-js');
  let pricesArr = [];
  for (i = 0; i < prices.length; i++) {
    pricesArr.push(prices[i].innerText.replace(',', ''));
  }
  console.log(pricesArr);

  quantities = document.body.getElementsByClassName('qty-js');
  let quantitiesArr = [];
  for (i = 0; i < quantities.length; i++) {
    quantitiesArr.push(quantities[i].value);
  }
  console.log(quantitiesArr);
  let totalPrice = 0;
  for (i = 0; i < prices.length; i++) {
    totalPrice += parseInt(quantitiesArr[i]) * parseInt(pricesArr[i]);
  }

  $('#checkout-total').html(totalPrice.toLocaleString());
}
