#!/usr/bin/node
function factorial (num) {
  if (num === 0) {
    return (1);
  } else {
    return (factorial(num - 1) * num);
  }
}
const x = parseInt(process.argv[2]);
if (x) {
  const res = factorial(x);
  console.log(res);
} else {
  console.log(1);
}
