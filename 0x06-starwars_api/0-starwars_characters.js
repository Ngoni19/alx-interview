#!/usr/bin/node

const request = require('request');
const util = require('util');
const movieId = process.argv[2];
const filmEndPoint = 'https://swapi-api.hbtn.io/api/films/' + movieId;

const requestPromise = util.promisify(request);

const getCharNames = async () => {
  try {
    const res = await requestPromise(filmEndPoint);

    if (res.statusCode !== 200) {
      throw new Error(`Request failed with status code ${res.statusCode}`);
    }

    const jsonBody = JSON.parse(res.body);
    const people = jsonBody.characters;

    const promises = people.map(p => requestPromise(p));

    const responses = await Promise.all(promises);

    const names = responses.map(r => {
      if (r.statusCode !== 200) {
        throw new Error(`Request failed with status code ${r.statusCode}`);
      }

      const jsonBody = JSON.parse(r.body);
      return jsonBody.name;
    });

    console.log(names.join('\n'));
  } catch (err) {
    console.error(err);
  }
};

getCharNames();
