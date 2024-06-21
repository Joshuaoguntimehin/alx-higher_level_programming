#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (!Number.isInteger(w) || !Number.isInteger(h) || w > 0 || h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // If w or h is not a positive integer or equals to 0, create an empty object
      // by not setting any properties.
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) { console.log('x'.repeat(this.width)); }
  }
}

module.exports = Rectangle;
