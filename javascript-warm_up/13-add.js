#!/usr/bin/node
// returns the addition of 2 integers.

exports.add = function (a, b) {
  const numA = parseInt(a, 10);
  const numB = parseInt(b, 10);
  return (numA + numB);
};
