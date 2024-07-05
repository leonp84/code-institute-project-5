$(function () {
  // Dynamically update the minimum and maximum price range indicators upon user interaction

  $('#minimum-price').on('change', function () {
    let updateVal = $('#minimum-price').val();
    $('#min-price-display').text(updateVal);
  });

  $('#maximum-price').on('change', function () {
    let updateVal = $('#maximum-price').val();
    $('#max-price-display').text(updateVal);
  });
});
