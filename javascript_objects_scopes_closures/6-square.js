#!/usr/bin/node
// defines a square and inherits from Rectangle of 4-rectangle.js
const Square = require('./5-square.js');

class Square2 extends Square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let indH = 0; indH < this.height; indH++) {
      let sizeC = '';
      for (let indW = 0; indW < this.width; indW++) {
        sizeC += c;
      }
      console.log(sizeC);
    }
  }
}

module.exports = Square2;
