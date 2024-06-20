$(function () {
  bag = window.localStorage.getItem('shoppingBagTotal');
  if (bag != null) {
    $('.bag-items-number').text(bag);
    $('.bag-items-number').show();
  }
});
