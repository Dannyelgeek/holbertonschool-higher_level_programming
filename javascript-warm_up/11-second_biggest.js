#!/usr/bin/node
// searches the second biggest integer in the list of arguments.

const passedArgs = process.argv.slice(2).map(Number);

function secondBiggest (nums) {
  nums.sort(function (a, b) {
    return b - a;
  });
  return nums[1];
}

if (!passedArgs[0]) {
  console.log('0');
} else if (passedArgs.length === 1 && passedArgs[0] === 1) {
  console.log('0');
} else {
  console.log(secondBiggest(passedArgs));
}
