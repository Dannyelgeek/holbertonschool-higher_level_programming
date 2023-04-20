#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number matches a given integer.
const passedArg = process.argv.slice(2);
const request = require('request');

request.get(passedArg[0], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const moviesInfo = JSON.parse(body).results;
  console.log(moviesInfo.reduce((count, films) => {
    return films.characters.find((person) => person.endsWith('/18/'))
      ? count + 1
      : count;
  }, 0));
});
