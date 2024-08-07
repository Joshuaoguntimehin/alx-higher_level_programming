src="https://code.jquery.com/jquery-3.2.1.min.js"
$(document).ready(function() {
    console.log("jQuery is working");
    $('#add_item').click(function() {
      $('<li>Item</li>').appendTo('.my_list');
    });
  });
  