#!/usr/bin/node
/*
 * A class Rectangle that defines a rectangle.
 * constructor arguments:
 *   width = w
 *   height = h
 * Creates an empty object if w or h is less than or equal to zero.
 * Print(): Prints a rectangle
 */

module.exports = class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && Number.isInteger(h) && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let occurrenceX = 'X';
    for (let i = this.width; i > 1; i--) {
      occurrenceX += 'X';
    }
    for (let j = this.height; j > 0; j--) {
      console.log(occurrenceX);
    }
  }
};
