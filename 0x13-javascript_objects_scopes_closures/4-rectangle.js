#!/usr/bin/node

/* happy codeing express */
class Rectangle {
  constructor (w, h) {
		 if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
			 return object.create(null);
		 }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
