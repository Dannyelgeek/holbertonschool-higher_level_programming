#!/usr/bin/node
// display the status code of a GET request.
const passedArg = process.argv.slice(2);

const request = require('request');
request(passedArg[0], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log('code:', response && response.statusCode);
});
