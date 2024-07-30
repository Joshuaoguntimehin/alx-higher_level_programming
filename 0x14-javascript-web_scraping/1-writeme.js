#!/usr/bin/node
const fs = require('fs');
const path = require('path');

// Check if the correct number of arguments is provided
if (process.argv.length < 4) {
    console.error('Usage: node writeFile.js <file-path> <data-to-write>');
    process.exit(1);
}

// Get the file path and data from command-line arguments
const filePath = process.argv[2];
const data = process.argv[3];

// Validate inputs
if (!filePath || !data) {
    console.error('Error: File path and data must be provided.');
    process.exit(1);
}

// Resolve file path
const resolvedPath = path.resolve(filePath);

// Write the data to the file asynchronously
fs.writeFile(resolvedPath, data, 'utf8', (err) => {
    if (err) {
        console.error(`Error writing to the file: ${err.message}`);
        return;
    }
    console.log(data);
});
