#!/usr/bin/node

function add (a, b) {
  return (a + b);
}

const fInt = parseInt(process.argv[2]);
const sInt = parseInt(process.argv[3]);

if (isNaN(fInt) || isNaN(sInt)) {
  console.log('NaN');
} else {
  console.log(add(fInt, sInt));
}
