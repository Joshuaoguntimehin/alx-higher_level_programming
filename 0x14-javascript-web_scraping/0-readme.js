#!/usr/bin/node
"""const argument """
const args = process.argv.slice(2);
const fs = require('fs');

const filePath = process.argv[2];

// Read the file using utf-8 encoding
fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
        // Print the error object if an error occurs
        console.error(err);
    } else {
        // Print the file content
        console.log(data);
    }
});
