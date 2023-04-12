#!/usr/bin/node
exports.list = [1, 2, 3, 4, 5];
const map1 = list.map((x, index) => x * index);
console.log(map1);
