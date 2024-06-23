$(function () {
  $('.remove-from-wishlist').on('click', function () {
    productId = $(this).next().text();
    // AJAX POST Request
    // The CSFR_TOKEN variable below is provided at the bottom of the base HTML file
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
        console.log(response.message);
      },
      error: function (xhr, status, error) {
        console.error('Error:', error);
      },
    });

    $(this).parent().remove();
    let itemRemovedToast = bootstrap.Toast.getOrCreateInstance(
      $('#item-removed-toast')
    );
    itemRemovedToast.show();
  });
});
