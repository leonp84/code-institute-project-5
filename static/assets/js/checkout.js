$(function () {
  $('#discount-code-form').on('submit', function (e) {
    e.preventDefault();
    $('#code-submit-button').html(
      `<span>Checking...</span>
          <div class="spinner-border spinner-border-sm" role="status"></div>`
    );
    $('#code-submit-button').attr('disabled', 'true');
    $('#discount-code-input').attr('disabled', 'true');

    setTimeout(() => {}, '1500');

    code = $('#discount-code-input').val();
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
          console.log(response.message);
          $('#code-error').hide();
          $('#code-success').show();
          $('#code-submit-button').html('Code Valid');
          updatePrice();
        } else {
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
 *
 */
function updatePrice() {
  currentAmount = parseInt($('#amount-to-pay').text().replace(',', ''));
  console.log(currentAmount);
  newAmount = currentAmount - 100;
  console.log(newAmount);
  $('#amount-to-pay').text(newAmount.toLocaleString());
  $('#amount-to-pay-form').val(newAmount);
}
