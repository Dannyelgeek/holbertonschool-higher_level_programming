#!/usr/bin/node
// script that prints a square

const passedArg = process.argv.slice(2);
const num = parseInt(passedArg, 10);

if (!passedArg[0]) {
  console.log('Missing number of occurrences');
} else {
  for (let ind = 0; ind < num; ind++) {
    let sizeX = '';
    for (let ind2 = 0; ind2 < num; ind2++) {
      sizeX += 'X';
    }
    console.log(sizeX);
  }
}
