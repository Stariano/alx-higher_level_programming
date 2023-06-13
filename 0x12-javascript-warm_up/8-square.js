#!/usr/bin/node
const process = require('process');

const args = process.argv;

const myInt = parseInt(args[2]);

if (isNaN(myInt)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myInt; i++) {
    let row = '';
    for (let j = 0; j < myInt; j++) row += 'X';
    console.log(row);
  }
}
