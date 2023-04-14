#!/usr/bin/node
// prints the first argument passed to it.

const passedArgs = process.argv.slice(2);

console.log(`${passedArgs[0] || 'No argument'}`);
