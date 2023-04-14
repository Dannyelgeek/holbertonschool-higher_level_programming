#!/usr/bin/node
// prints a message depending of the number of arguments passed

process.argv.forEach((val, ind) => {
    if(ind === 1){
        console.log('No argument');
    } else if(ind === 2){
        console.log('Argument found');
    } else if(ind >= 3){
        console.log('Arguments found');
    }
});
