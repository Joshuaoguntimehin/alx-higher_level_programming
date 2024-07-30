#!/usr/bin/node
const request = require('request');

// Get the URL from the command line arguments
const url = process.argv[2];

if (!url) {
  console.error('Please provide a URL as the first argument.');
  process.exit(1);
}

// Perform a GET request to the specified URL
request(url, (error, response) => {
  if (error) {
    console.error('An error occurred:', error);
  } else {
    // Print the status code in the specified format
    console.log(`code: ${response.statusCode}`);
  }
});
