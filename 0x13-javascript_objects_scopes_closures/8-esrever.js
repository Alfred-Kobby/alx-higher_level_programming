#!/usr/bin/node
exports.esrever = function (list) {
  const size = list.length;
  let j = 0;
  let reverseArr = [];
  for (let i = size; i >= 0; i--) {
    reverseArr[j] = list[i];
    j++;
  }
  return reverseArr;
}
