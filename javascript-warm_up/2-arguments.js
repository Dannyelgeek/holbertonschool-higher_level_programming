#!/usr/bin/node
// prints a message depending of the number of arguments passed
import { argv } from 'node:process';


argv.forEach((val, index) => {
    if(index <= 2){
        console.log('No argument');
    }
    if(index === 3){
        console.log('Argument found');
    }
    else{
        console.log('Arguments found');
    }
});
