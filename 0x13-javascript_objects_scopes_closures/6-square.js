#!/usr/bin/node
// A class Square that defines a square and inherits from Square of 5-square.js

const formerSquare = require('./5-square');

module.exports = class Square extends formerSquare {
  charPrint (c) {
    c === undefined ? this.print() : this.print(c);
  }
};
