#!/usr/bin/node

function isEmpty (value) {
  return (value == null || (typeof value === 'string' && value.trim().length === 0));
}

const process = require('process');

const args = process.argv;

if (isEmpty(args[2])) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
