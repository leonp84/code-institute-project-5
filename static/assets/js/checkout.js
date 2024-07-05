$(function () {
  // Check for discount code submission
  $('#discount-code-form').on('submit', function (e) {
    e.preventDefault();
    $('#code-submit-button').html(
      `<span>Checking...</span>
          <div class="spinner-border spinner-border-sm" role="status"></div>`
    );
    $('#code-submit-button').attr('disabled', 'true');
    $('#discount-code-input').attr('disabled', 'true');

    setTimeout(() => {}, '1500');

    // AJAX post request to check discount code validity
    let code = $('#discount-code-input').val();
    $.ajax({
      url: '/my_account/check_discount_code/',
      type: 'POST',
      data: JSON.stringify({
        code: code,
      }),
      dataType: 'json',
      headers: {
        'X-Requested-With': 'XMLHttpRequest',
        'X-CSRFToken': CSRF_TOKEN,
      },
      success: function (response) {
        if (response.status === 'ok') {
          // If code valid: Show success message and update price
          $('#code-error').hide();
          $('#code-success').show();
          $('#code-submit-button').html('Code Valid');
          updatePrice();
        } else {
          // If code invalid: Show error message and allow customer to try again
          $('#code-success').hide();
          $('#code-error').show();
          $('#code-submit-button').attr('disabled', false);
          $('#discount-code-input').attr('disabled', false);
          $('#code-submit-button').html('Check Again');
        }
      },
      error: function (xhr, status, error) {
        console.error(error);
      },
    });
  });
});

/*
 * Dynamically update the price when a valid discount code is used.
 */
function updatePrice() {
  let currentAmount = parseInt($('#amount-to-pay').text().replace(',', ''));
  let newAmount = currentAmount - 100;
  $('#amount-to-pay').text(newAmount.toLocaleString());
  $('#amount-to-pay-form').val(newAmount);
}
