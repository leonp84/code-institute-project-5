$(function () {
  bag = window.localStorage.getItem('shoppingBag');
  if (bag != null) {
    $('#bag-items-number').text(bag);
    $('#bag-items-number').show();
  }
});
