#!/usr/bin/node
// returns the reversed version of a list.

exports.esrever = function (list) {
  const newList = [];
  for (let ind = list.length - 1; ind >= 0; ind--) {
    newList.push(list[ind]);
  }
  return newList;
};
