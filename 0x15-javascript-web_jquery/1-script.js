$(document).ready(function() {
    // Add a click event handler to the <div> with ID 'red_header'
    $('#red_header').on('click', function() {
        // Add the class 'red' to the <header> element
        $('header').addClass('red');
    });
});
