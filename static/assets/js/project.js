$(function () {
  bag = window.localStorage.getItem('shoppingBagTotal');
  if (bag != null) {
    $('.bag-items-number').text(bag);
    $('.bag-items-number').show();
  }

  allTextInputs = document.body.getElementsByTagName('input');
  for (i = 0; i < allTextInputs.length; i++) {
    allTextInputs[i].addEventListener('invalid', (e) => {
      e.target.classList.add('error');
      let errorMsg = document.createElement('div');
      errorMsg.innerHTML = `<span>This input is not valid</span>`;
      errorMsg.classList.add('error');
      e.target.parentNode.appendChild(errorMsg);
      console.log(e.srcElement);
      console.log(e.target);
    });
  }
});
