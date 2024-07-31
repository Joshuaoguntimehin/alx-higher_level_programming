#!/usr/bin/node
// Check if the correct number of arguments is provided
if (process.argv.length < 4) {
  console.error('Usage: node writeFile.js <url> <file-path>');
  process.exit(1);
}

const fs = require('fs');
const request = require('request');

// Retrieve URL and file path from the command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a request to the URL
request(url, (error, response, body) => {
  if (error) {
    console.error('Error fetching URL:', error);
    return;
  }

  // Check if the response status code is OK
  if (response.statusCode !== 200) {
    console.error('Failed to fetch the URL. Status code:', response.statusCode);
    return;
  }

  // Write the response body to the file
  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.error('Error writing file:', err);
      return;
    }
    console.log(`Data from ${url} has been written to ${filePath}`);
  });
});
