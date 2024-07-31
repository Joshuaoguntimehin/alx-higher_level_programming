#!/usr/bin/node
const request = require('request');
const url =  process.argv[2];
const id = 0;
for (i = 0, i = id, i++);
console.log(id)
request (url, function (error, response, body) {
 if (error) {
  console.log(error);
 } else {
  console.log(JSON.parse(body).completed);
 }
});
