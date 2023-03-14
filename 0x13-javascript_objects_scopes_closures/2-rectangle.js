#!/usr/bin/node
/*
 * A class Rectangle that defines a rectangle.
 * constructor arguments:
 *   width = w
 *   height = h
 * Creates an empty object if w or h is less than or equal to zero.
 */

module.exports = class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && Number.isInteger(h) && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
