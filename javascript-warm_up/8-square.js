#!/usr/bin/node
// script that prints a square

const passedArg = process.argv.slice(2);
const num = parseInt(passedArg, 10);

if (!passedArg[0]) {
  console.log('Missing size');
} else if (isNaN(num) === true) {
  console.log('Missing size');
} else {
  for (let ind = 0; ind < num; ind++) {
    let sizeX = '';
    for (let ind2 = 0; ind2 < num; ind2++) {
      sizeX += 'X';
    }
    console.log(sizeX);
  }
}
