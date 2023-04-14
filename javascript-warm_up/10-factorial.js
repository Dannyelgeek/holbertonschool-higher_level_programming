#!/usr/bin/node
// computes and prints a factorial

const passedArgs = process.argv.slice(2);
const passedNum1 = parseInt(passedArgs[0], 10);

function fact (num) {
  let fac = 1;
  for (let ind = 1; ind <= passedNum1; ind++) {
    fac *= ind;
  }
  console.log(fac);
}

fact(passedNum1);
