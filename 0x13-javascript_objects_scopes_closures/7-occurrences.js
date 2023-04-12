#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let numOccurence = 0;
  for (const i of list) {
    if (i === searchElement) {
      numOccurence++; 
    }
  }
  return numOccurence;
}
