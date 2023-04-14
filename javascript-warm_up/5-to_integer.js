#!/usr/bin/node
// prints My number: <first argument converted in integer> if the first argument can be converted to an integer.

const passedArg = process.argv.slice(2);
let num = parseInt(passedArg, 10);

if (!passedArg[0]) {
  console.log('Not a number');
} else if (isNaN(num) === true) {
    console.log('Not a number');
} else if (typeof num === "number") {
    console.log('My number:', num);
}