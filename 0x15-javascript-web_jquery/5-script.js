$(document).ready(function () {
  $('#add_item').click(function () {
    const newItem = $('<li></li>').text('Item');
    $('ul.my_list').append(newItem);
  });
});

/*
const addItem = document.querySelector('div#add_item');
addItem.addEventListener('click', function() {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    const ulMyList = document.querySelector('ul.my_list');
    ulMyList.appendChild(newItem);
})
*/
