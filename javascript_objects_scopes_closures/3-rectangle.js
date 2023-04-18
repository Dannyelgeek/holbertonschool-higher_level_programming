#!/usr/bin/node
// defines a rectangle class.

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      // empty
    } else if (w === undefined || h === undefined) {
      // empty
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let indH = 0; indH < this.height; indH++) {
      let sizeX = '';
      for (let indW = 0; indW < this.width; indW++) {
        sizeX += 'X';
      }
      console.log(sizeX);
    }
  }
}

module.exports = Rectangle;
