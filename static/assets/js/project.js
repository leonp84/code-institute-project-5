$(function () {
  // Trigger extra newsletter signup when user has scrolled at least 50% to page bottom
  let runOnce = false;
  $(window).on('scroll', function () {
    if ($(window).scrollTop() > 500 && !runOnce) {
      runOnce = true;
      $('#hidden-newsletter').show();
      $('#newsletter-close-button').on('click', function () {
        $('#hidden-newsletter').remove();
      });
      // Update Django session variable if newsletter shown
      $.ajax({
        url: '/newsletter_shown/',
        type: 'POST',
        data: JSON.stringify({
          newsletterShown: true,
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
    }
  });

  if (parseInt($('.bag-items-number').first().text()) !== 0) {
    $('.bag-items-number').show();
  }

  // Initialize all Bootstrap Tooltips on page
  var tooltipTriggerList = [].slice.call(
    document.querySelectorAll('[data-bs-toggle="tooltip"]')
  );
  var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
  });

  allTextInputs = document.body.getElementsByTagName('input');
  for (i = 0; i < allTextInputs.length; i++) {
    allTextInputs[i].addEventListener('invalid', (e) => {
      e.target.classList.add('error');
      let errorMsg = document.createElement('div');
      errorMsg.innerHTML = `<span>This input is not valid</span>`;
      errorMsg.classList.add('error');
      e.target.parentNode.appendChild(errorMsg);
    });
  }

  // Eventlistener for search icon to reveal search bar
  $('.search-icon').on('click', function (e) {
    e.preventDefault();
    $('#search-box').toggle();
    $('#search-box').find('input').focus();
  });

  $('#search-scrolling-bar').on('click', function (e) {
    $('#search-box').toggle();
    $('#search-box').find('input').focus();
  });
});
