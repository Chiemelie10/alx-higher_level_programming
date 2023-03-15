#!/usr/bin/mode
// A class Square that defines a square and inherits from a Rectangle of 4-rectangle.js

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
