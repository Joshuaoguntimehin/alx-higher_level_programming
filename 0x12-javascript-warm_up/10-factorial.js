#!/usr/bin/node
function factorial(n) {
    if (isNaN(n)) {
        return 1;
    }
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

// Read the argument, cast it to an integer
const input = parseInt(process.argv[2], 10);

// Compute the factorial of the input
const result = factorial(input);

// Print the result
console.log(result);

