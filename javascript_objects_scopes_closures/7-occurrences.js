#!/usr/bin/node
// returns the number of occurrences in a list.

exports.nbOccurences = function (list, searchElement) {
  let occ = 0;
  for (let ind = 0; ind < list.length; ind++) {
    if (list[ind] === searchElement) {
      occ++;
    }
  }
  return occ;
};
