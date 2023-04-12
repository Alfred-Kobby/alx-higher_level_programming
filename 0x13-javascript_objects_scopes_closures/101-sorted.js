#!/usr/bin/node
const dict = require('./101-data.js').dict;
const myDict = {};
for (const key in dict) {
  if (!newDict[dict[key]]) {
    myDict[dict[key]] = [];
  }
  myDict[dict[key]].push(key);
}
console.log(myDict);
