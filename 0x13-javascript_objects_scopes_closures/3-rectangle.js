#!/usr/bin/node
class Rectangle {
    constructor(w, h) {
        if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
            // If w or h is 0 or not a positive integer, create an empty object
            return Object.create(null);
        }

        // Initialize the attributes only if w and h are positive integers
        this.width = w;
        this.height = h;
    }

    // Instance method to print the rectangle using the character 'X'
    print() {
        for (let i = 0; i < this.height; i++) {
            console.log('x'.repeat(this.width));
	}
    }
}
module.exports = Rectangle;
