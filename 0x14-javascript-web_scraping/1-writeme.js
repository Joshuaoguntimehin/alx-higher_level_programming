#!/usr/bin/node
""" Import the file system module"""
const fs = require('fs');

""" Check if the correct number of arguments is provided"""
if (process.argv.length < 4) {
  console.error('Usage: node writeFile.js <file-path> <data-to-write>');
  process.exit(1);
}

// Get the file path and data from command-line arguments
const filePath = process.argv[2];
const data = process.argv[3];

// Write the data to the file asynchronously
fs.writeFile(filePath, data, 'utf8', (err) => {
	if (err) {
		// Handle the error if there is one
		console.error('Error writing to the file:', err.message);
		return;
	}
	// Confirm that the file was written successfully
	console.log(data);
});
