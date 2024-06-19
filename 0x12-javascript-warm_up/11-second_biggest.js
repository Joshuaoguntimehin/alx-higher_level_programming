#!/usr/bin/node
function findSecondBiggest (args) {
  if (args.length < 2) {
    return 0;
  }

  // Convert arguments to integers and sort them in descending order
  const integers = args.map(arg => parseInt(arg, 10)).sort((a, b) => b - a);

  // Return the second biggest integer
  return integers[1];
}

// Read command-line arguments (ignoring the first two default arguments)
const args = process.argv.slice(2);

// Find the second biggest integer
const result = findSecondBiggest(args);

// Print the result
console.log(result);
