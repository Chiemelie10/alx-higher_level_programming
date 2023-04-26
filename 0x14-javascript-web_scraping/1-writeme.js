#!/usr/bin/node
// This script writes a string to a file

const fs = require('fs');
const filePath = process.argv[2];
const data = process.argv[3];

fs.writeFile(filePath, data, 'utf-8', function (err) {
  if (err) {
    console.log(err);
  }
});
