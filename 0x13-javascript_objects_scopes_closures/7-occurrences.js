#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  // Initialize a counter to keep track of occurrences
  let count = 0;

  // Iterate through each element in the list
  for (let i = 0; i < list.length; i++) {
    // Check if the current element matches the searchElement
    if (list[i] === searchElement) {
      // Increment the counter if there's a match
      count++;
    }
  }

  // Return the total count of occurrences
  return count;
};
