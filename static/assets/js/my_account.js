$(function () {
  // Check for when customer wants to remove item from wishlist
  $('.remove-from-wishlist').on('click', function () {
    let productId = $(this).next().text();
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
    // Display toast to confirm wishlist updated
    $(this).parent().remove();
    let itemRemovedToast = bootstrap.Toast.getOrCreateInstance(
      $('#item-removed-toast')
    );
    itemRemovedToast.show();
  });
  // Dynamically update 'Edit Product' and 'Delete Product' buttons when customer chooses a product from the select-product-box list
  $('#select-product-box').on('change', function () {
    if ($(this).val() == 0) {
      $('#edit-product-button').addClass('disabled');
      $('#delete-product-button').addClass('disabled');
    } else {
      let id = $(this).val();
      $('#edit-product-button').removeClass('disabled');
      $('#edit-product-button').attr('href', `/product/edit_product/${id}`);
      $('#delete-product-button').removeClass('disabled');
      $('#delete-product-button').attr('href', `/product/delete_product/${id}`);
    }
  });
});
