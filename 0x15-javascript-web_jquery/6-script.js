$(document).ready(function () {
  $('div#update_header').on('click', function () {
    $('header').text('New Header!!!');
  });
});

/*
const updateHeader = document.querySelector('div#update_header');
updateHeader.addEventListener('click', function() {
    const header = document.querySelector('header');
    header.textContent = 'New Header!!!';
});
*/
