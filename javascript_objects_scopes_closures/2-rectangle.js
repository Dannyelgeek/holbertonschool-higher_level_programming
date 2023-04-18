#!/usr/bin/node
// defines a rectangle class.

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      // empty
    } else if (w === undefined || h === undefined) {
      //empty
    }else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
