$(document).ready(function() {
    // Define the API URL
    var apiUrl = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  
    // Perform an AJAX GET request to the API
    $.get(apiUrl, function(data) {
      // Extract the character name from the response data
      var characterName = data.name;
  
      // Update the content of the DIV#character element with the character name
      $('#character').text(characterName);
    }).fail(function() {
      // In case of an error, update the content to indicate failure
      $('#character').text('Failed to load character data');
    });
  });
  