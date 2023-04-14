#!/usr/bin/node
// prints the addition of 2 integers

const passedArgs = process.argv.slice(2);
const passedNum1 = parseInt(passedArgs[0], 10);
const passedNum2 = parseInt(passedArgs[1], 10);

function add (a, b) {
  console.log(a + b);
}

add(passedNum1, passedNum2);
