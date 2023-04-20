#!/usr/bin/node
// gets the contents of a webpage and stores it in a file.
const passedArg = process.argv.slice(2);
const request = require('request');
const fs = require('fs');

request(passedArg[0]).pipe(fs.createWriteStream(passedArg[1]));
