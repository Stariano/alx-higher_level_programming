#!/usr/bin/node

exports.esrever = function (list) {
  const listt = [];
  let itr = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    listt[itr] = list[i];
    itr++;
  }
  return listt;
};
