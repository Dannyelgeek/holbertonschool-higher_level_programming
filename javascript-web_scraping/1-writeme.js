#!/usr/bin/node
// writes a string to a file.
const fs = require('fs');

const passedArg = process.argv.slice(2);

fs.appendFile(passedArg[0], passedArg[1], 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
