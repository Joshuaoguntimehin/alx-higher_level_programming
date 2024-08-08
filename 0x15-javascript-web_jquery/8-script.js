// 8-script.js
$(document).ready(function() {
    // Define the API URL
    const apiUrl = 'https://swapi-api.alx-tools.com/api/films/?format=json';
    
    // Use jQuery's AJAX method to fetch data from the API
    $.ajax({
        url: apiUrl,
        method: 'GET',
        dataType: 'json',
        success: function(data) {
            // Extract the films array from the response data
            const films = data.results;
            
            // Iterate over the films array
            films.forEach(function(film) {
                // Create a new list item element
                const listItem = $('<li>').text(film.title);
                
                // Append the list item to the <ul> with id list_movies
                $('#list_movies').append(listItem);
            });
        },
        error: function(jqXHR, textStatus, errorThrown) {
            // Handle any errors that occur during the request
            console.error('Error fetching the movies:', textStatus, errorThrown);
        }
    });
});
