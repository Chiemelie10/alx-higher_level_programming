#!/usr/bin/node
// A function that returns the reversed version of a list

exports.esrever = function (list) {
  let listLength = list.length;
  for (let i = 0; i < listLength; i++, listLength--) {
    const temp = list[i];
    list[i] = list[listLength - 1];
    list[listLength - 1] = temp;
  }
  return list;
};
