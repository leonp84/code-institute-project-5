$(function () {
  $('.watch-extra-images').on('click', function () {
    let newImage = $(this).attr('src');
    $('.main-product-image').attr('src', newImage);
    $('#modal-image').attr('src', newImage);
    $('.watch-extra-images').css('border', '1px solid black');
    $(this).css('border', '1px solid rgb(208, 177, 20)');
  });

  $('.main-product-image').on('click', function () {
    $('#largeImageModal').modal('show');
  });
});
