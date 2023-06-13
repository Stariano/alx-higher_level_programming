#!/usr/bin/node

const args = process.argv;
const values = [];

if (isNaN(parseInt(args[2]))) {
  console.log(0);
} else if (args.length === 3) {
  console.log(0);
} else {
  for (let i = 2; i < args.length; i++) {
    values.push(args[i]);
  }
  const unique = [...new Set(values)];
  unique.sort(function (a, b) { return a - b; });
  console.log(unique[unique.length - 2]);
}
