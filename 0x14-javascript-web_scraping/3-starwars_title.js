#!/usr/bin/node
/**
 * This script the title of a Star Wars movie where the
 * episode number matches a given integer.
 */

const request = require('request');
const StarWarsApi = 'https://swapi-api.alx-tools.com/api/films/';
const episodeNum = process.argv[2];
const url = StarWarsApi + episodeNum;

request(url, function (error, response, body) {
  if (error === null) {
    const JavaScriptObj = JSON.parse(body);
    const StarWarsTitle = JavaScriptObj.title;
    console.log(StarWarsTitle);
  }
});
