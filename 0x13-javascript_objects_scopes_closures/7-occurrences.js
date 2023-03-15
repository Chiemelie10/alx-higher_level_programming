#!/usr/bin/node
// A function that returns the number of occurrences in a list.

exports.nbOccurences = function (list, searchElement) {
  let elementFound = 0;

  for (const element of list) {
    if (element === searchElement) {
      elementFound += 1;
    }
  }
  return elementFound;
};
