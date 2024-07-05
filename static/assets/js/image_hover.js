$(function () {
  // Preload Images for faster transition effect
  window.onload = () => {
    preloadImages(images);
  };

  const images = [];

  $('.main-image').each(function () {
    let currentImage = $(this).attr('src');
    let newImage = currentImage.slice(0, currentImage.length - 6);
    newImage += '2.webp';
    images.push(newImage.toString());
  });

  // The preloadImages function below was copied and slightly adapted from code provided by ChatGPT
  const preloadImages = (srcArray) => {
    srcArray.forEach((src) => {
      const img = new Image();
      img.src = src;
    });
  };

  // Product List Display Image Hover Effect
  $('.main-image').on('mouseover', function () {
    let currentImage = $(this).attr('src');
    let newImage = currentImage.slice(0, currentImage.length - 6);
    newImage += '2.webp';
    $(this).attr('src', newImage);
    $(this).css('transform', 'scale(1.7) translate(20px, 20px)');
    $(this).css('transition', '1s');
    $('.main-image').on('mouseout', function () {
      $(this).attr('src', currentImage);
      $(this).css('transform', 'scale(1)');
      $(this).css('transition', '0.5s');
    });
  });
});
