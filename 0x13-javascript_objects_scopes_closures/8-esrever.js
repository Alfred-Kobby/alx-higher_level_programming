#!/usr/bin/node
exports.esrever = function (list) {
  const size = list.length - 1;
  let reverseArr = [];
  for (let i = size; i >= 0; i--) {
    reverseArr.push(list[i]);
  }
  return reverseArr;
};
