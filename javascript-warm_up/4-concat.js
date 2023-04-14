#!/usr/bin/node
// prints two arguments passed to it, in the following format: "is".

const passedArgs = process.argv.slice(2);

console.log(passedArgs[0], 'is', passedArgs[1]);
