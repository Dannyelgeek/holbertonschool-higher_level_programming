#!/usr/bin/node
// prints x times 'C is fun'

const cStr = 'C is fun';
const passedArg = process.argv.slice(2);
const num = parseInt(passedArg, 10);

if (!passedArg[0]) {
  console.log('Missing number of occurrences');
} else {
  for (let ind = 0; ind < num; ind++) {
    console.log(cStr);
  }
}
