$(function () {
  // Delay CSS Animation triggers until object in view
  let mainProductList = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        $(entry.target).addClass('animate__fadeInUp');
      }
    });
  });
  mainProductList.observe(document.querySelector('#product-images-homepage'));

  let motivationText = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        $(entry.target).addClass('animate__fadeInRight');
      }
    });
  });
  motivationText.observe(document.querySelector('#motivation-text'));
});
