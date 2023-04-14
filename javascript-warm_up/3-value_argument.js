#!/usr/bin/node
// prints the first argument passed to it.

const argsPassed = process.argv.slice(2);
let count = 0;
let argsBySpace = '';

for (const arg of argsPassed) {
  count++;
}

if (count === 0) {
  console.log('No arguments');
} else {
  argsPassed.forEach((val, ind) => {
    argsBySpace += val + ' ';
  });
  console.log(argsBySpace);
}
