#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const argv = process.argv;
  const array = argv.slice(2).sort((a, b) => a - b).reverse();
  console.log(array[1]);
}
