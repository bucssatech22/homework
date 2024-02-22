document.addEventListener('DOMContentLoaded', function () {
  const submitButton = document.querySelector('form button[type="submit"]');
  const cartIcon = document.getElementById('cart-icon');
  let animationCompleted = false;

  submitButton.addEventListener('click', function (event) {
    if (!animationCompleted) {
      event.preventDefault();
      let flyingImage = document.createElement('img');
      flyingImage.src = '/static/pictures/face.png';
      flyingImage.classList.add('flying-image');
      document.body.appendChild(flyingImage);

      let start = submitButton.getBoundingClientRect();
      let end = cartIcon.getBoundingClientRect();

      flyingImage.style.left = start.left + 'px';
      flyingImage.style.top = start.top + 'px';

      setTimeout(function () {
        flyingImage.style.left = end.left + 'px';
        flyingImage.style.top = end.top + 'px';
      }, 100);

      setTimeout(function () {
        flyingImage.remove();
        animationCompleted = true;
        submitButton.click(); //  click the submit button to submit the form
      }, 1000); //disappear time
    }
  });
});
