#!/usr/bin/node
// reads and prints the content of a file.
const fs = require('fs');

const passedArg = process.argv.slice(2);

fs.readFile(passedArg[0], 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
