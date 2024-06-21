#!/usr/bin/node

exports.converter = function (base) {
  if (!Number.isInteger(base) || base < 2 || base > 36) {
    throw new Error('The base must be an integer between 2 and 36');
  }
  return function (number) {
    if (!Number.isInteger(number)) {
      throw new Error('The number must be an integer');
    }
    return number.toString(base);
  };
};
