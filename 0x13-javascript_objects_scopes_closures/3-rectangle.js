#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      class Rectangle {//enpty}
    }
    this.width = w;
    this.height = h;
  }
	  print() {
		  if (!this.width || !this.height) {
			  console.log('rectangle is empty');
			  return;
		  }
		  for (let i = 0; i < this.height; i++) {
			  let row = '';
		  }
		  for (let j = 0; j < this.width; j++) {
			  row += 'x';
		  }
		  console.log(row);
	  }
  }
}
module.exports = Rectangle;
