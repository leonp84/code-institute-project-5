$(function () {
  let productId = parseInt($('#product-id').text());
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
    if (window.localStorage.getItem('shoppingBag') === null) {
      firstProduct = {
        quantity: 1,
        product: productId,
      };
      window.localStorage.setItem('shoppingBag', JSON.stringify(firstProduct));
      $('#bag-items-number').text('1');
      $('#bag-items-number').show();

      //   retrievedProduct = window.localStorage.getItem('shoppingBag');
      //   console.log(JSON.parse(retrievedProduct).quantity);
    } else {
      itemsInCart = parseInt(window.localStorage.getItem('shoppingBag'));
      itemsInCart += 1;
      window.localStorage.setItem('shoppingBag', itemsInCart);
      $('#bag-items-number').text(itemsInCart);
    }
  });
});
