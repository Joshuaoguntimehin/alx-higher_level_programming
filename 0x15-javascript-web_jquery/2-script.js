// Wait for the document to be ready
$(document).ready(function() {
  // Select the #red_header div and attach a click event handler
  $('#red_header').on('click', function() {
    // Select the header element and change its text color to red
    $('header').css('color', '#FF0000');
  });
});
  