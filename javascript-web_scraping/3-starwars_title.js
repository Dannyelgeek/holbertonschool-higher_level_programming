#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number matches a given integer.
const passedArg = process.argv.slice(2);
const request = require('request');

request.get(`https://swapi-api.hbtn.io/api/films/${passedArg[0]}`, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const movieTitle = JSON.parse(response.body);
  console.log(movieTitle.title);
});
