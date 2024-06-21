#!/usr/bin/node
/* happy codeing express*/
class Rectangle {
  constructor (w, h) {
		 if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
			 // If w or h is 0 or not a positive integer, create an empty object
			 return object.create(null);
		 }

    // Initialize the attributes only if w and h are positive integers
    this.width = w;
    this.height = h;
  }

  // Instance method to print the rectangle using the character 'X'
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('x'.repeat(this.width));
    }
  }

  // Instance method to exchange the width and height of the rectangle
  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  // Instance method to multiply the width and height of the rectangle by 2
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
