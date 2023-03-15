#!/usr/bin/node
// A class Square that defines a square and inherits from a Rectangle of 4-rectangle.js

class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && Number.isInteger(h) && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (char = 'X') {
    let width = '';
    for (let i = 0; i < this.width; i++) {
      width += char;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(width);
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
