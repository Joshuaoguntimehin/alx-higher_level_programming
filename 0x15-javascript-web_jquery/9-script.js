// 9-script.js
$(function() {
    // Define the API URL
    const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
    
    // Use jQuery's AJAX method to fetch data from the API
    $.ajax({
        url: apiUrl,
        method: 'GET',
        dataType: 'json',
        success: function(data) {
            // Extract the "hello" value from the response data
            const helloTranslation = data.hello;
            
            // Set the text of the <div> with id "hello" to the translation
            $('#hello').text(helloTranslation);
        },
        error: function(jqXHR, textStatus, errorThrown) {
            // Handle any errors that occur during the request
            console.error('Error fetching the translation:', textStatus, errorThrown);
        }
    });
});
