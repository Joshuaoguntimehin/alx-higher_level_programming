#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    if (Number.isInteger(size) && size > 0) {
      super(size, size);
    } else {
      super(undefined, undefined); // This creates an empty object if size is invalid
    }
  }
}

module.exports = Square;
