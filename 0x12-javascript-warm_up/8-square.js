#!/usr/bin/node

const sizeSqr = process.argv[2];

if (isNaN(sizeSqr)) {
  console.log('Missing size');
} else {
  let value = 'X';
  for (let i = sizeSqr; i > 0 + 1; i--) {
    value += 'X';
  }
  for (let j = sizeSqr; j > 0; j--) {
    console.log(value);
  }
}
