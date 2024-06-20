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