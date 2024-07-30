#!/usr/bin/node

// Import the required module
const fs = require('fs');

// Retrieve command-line arguments, excluding the first two (node and script path)
const args = process.argv.slice(2);

// Get the file path from the arguments
const filePath = args[0];

// Read the file using UTF-8 encoding
fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
        // Print the error object if an error occurs
        console.error(err);
    } else {
        // Print the file content
        console.log(data);
    }
});
