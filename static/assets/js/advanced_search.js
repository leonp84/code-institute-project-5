$(function () {
  $('#minimum-price').on('change', function () {
    updateVal = $('#minimum-price').val();
    console.log(updateVal);
    $('#min-price-display').text(updateVal);
  });

  $('#maximum-price').on('change', function () {
    updateVal = $('#maximum-price').val();
    console.log(updateVal);
    $('#max-price-display').text(updateVal);
  });
});
