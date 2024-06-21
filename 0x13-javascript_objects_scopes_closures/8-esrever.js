#!/usr/bin/node
exports.esrever = function (list){
    for (let i = list.length -1; i >= 0; i--){
        process.stdout.write(`${list[i]}`)
    }   
}