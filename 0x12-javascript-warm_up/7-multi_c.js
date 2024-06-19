#!/usr/bin/node
const times = parseInt(process.argv[2]);
const message = 'C is fun';

if (!isNaN(times) && times > 0) {
  for (let i = 0; i < times; i++) {
    console.log(message);
  }
} else {
  console.log('Missing number of occurrences');
}
