$(function () {
  let productId = parseInt($('#product-id').text());

  let addedToast = bootstrap.Toast.getOrCreateInstance(
    $('#added-to-cart-toast')
  );

  $('.watch-extra-images').on('click', function () {
    let newImage = $(this).attr('src');
    $('.main-product-image').attr('src', newImage);
    $('#modal-image').attr('src', newImage);
    $('.watch-extra-images').css('border', '1px solid black');
    $(this).css('border', '1px solid rgb(208, 177, 20)');
  });

  $('.main-product-image').on('click', function () {
    $('#largeImageModal').modal('show');
    window.localStorage.clear();
  });

  $('#buy-button').on('click', function () {
    $('#buy-button').html(
      `<span>Adding...</span>
        <div class="spinner-border spinner-border-sm" role="status"></div>`
    );
    $('#buy-button').attr('disabled', true);
    $('#buy-button').css('background-color', 'grey');

    setTimeout(() => {
      addItemToBag();
      $('#buy-button').html('Add an additional item');
      $('#buy-button').attr('disabled', false);
      $('#buy-button').css('background-color', '#212529');
      addedToast.show();
    }, '3000');
  });
});

function addItemToBag() {
  if (window.localStorage.getItem('shoppingBagTotal') === null) {
    window.localStorage.setItem('shoppingBagTotal', 1);
    $('#bag-items-number').text('1');
    $('#bag-items-number').show();
  } else {
    itemsInCart = parseInt(window.localStorage.getItem('shoppingBagTotal'));
    itemsInCart += 1;
    window.localStorage.setItem('shoppingBagTotal', itemsInCart);
    $('#bag-items-number').text(itemsInCart);
  }
}
