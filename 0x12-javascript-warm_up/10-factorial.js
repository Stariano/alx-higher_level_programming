#!/usr/bin/node

function fact (a) {
  if (a === 1) {
    return 1;
  }
  return a * fact(a - 1);
}

const fInt = parseInt(process.argv[2]);

if (isNaN(fInt)) {
  console.log('1');
} else {
  console.log(fact(fInt));
}
