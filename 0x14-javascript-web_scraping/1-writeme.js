#!/usr/bin/node
// Import the file system module
const fs = require('fs');

// Get the file path and data from command-line arguments
const filePath = process.argv[2];
const data = process.argv[3];

// Write the data to the file asynchronously
fs.writeFile(filePath, data, 'utf8', (err) => {
  if (err) {
    // Handle the error if there is one
    console.error('Error writing to the file:', err.message);
  }
});
