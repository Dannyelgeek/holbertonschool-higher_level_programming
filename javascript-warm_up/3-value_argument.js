#!/usr/bin/node
//prints the first argument passed to it.

const argsPassed = process.argv.slice(2);
let argsBySpace = '';

if (argsPassed.length === 0) {
    console.log('No arguments');
} else {
    argsPassed.forEach((val ,ind) => {
        argsBySpace += val + ' ';
    });
    console.log(argsBySpace);
}
