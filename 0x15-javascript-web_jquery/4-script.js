$(document).ready(function () {
  $('#toggle_header').click(function () {
    const header = $('header');
    if (header.hasClass('red')) {
      header.removeClass('red');
      header.addClass('green');
    } else {
      header.removeClass('green');
      header.addClass('red');
    }
  });
});

/*
const toggleHeader = document.querySelector('div#toggle_header');
toggleHeader.addEventListener('click', function() {
    const header = document.querySelector('header');
    if (header.classList.contains('red')) {
        header.classList.remove('red');
        header.className = 'green';
    } else {
      header.classList.remove('green');
      header.className = 'red';
    }
});
*/
