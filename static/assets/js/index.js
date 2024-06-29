$(function () {
  // Delay CSS Animation triggers until object in view
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        $(entry.target).addClass('animate__fadeInUp');
      }
    });
  });
  observer.observe(document.querySelector('#product-images-homepage'));
});
